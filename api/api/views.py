import json

import pandas as pd
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Employee
from .paginations import StandardResultsSetPagination
from .serializers import EmployeeSerializer

DATAFRAME = None  # type: pd.Dataframe


def update_df():
    """
    Function that needs to be called when we make a change in the DB so that we will
    fetch again the dataframe
    """
    global DATAFRAME
    DATAFRAME = Employee.get_all_as_pandas_df()


def get_df() -> pd.DataFrame:
    if DATAFRAME is None:
        update_df()

    return DATAFRAME.copy()


# Employees endpoints

class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    pagination_class = StandardResultsSetPagination

    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = [
        "first_name",
        "last_name",
    ]
    filterset_fields = [
        "id",
        "first_name",
        "last_name",
        "email",
        "gender",
        "date_of_birth",
        "industry",
        "salary",
        "years_of_experience",
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get("sort", None)

        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset


class EmployeeGetView(APIView):
    def get(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class EmployeePostView(APIView):
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            update_df()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeePutView(APIView):
    def put(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)

        if serializer.is_valid():
            update_df()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDeleteView(APIView):
    def delete(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        update_df()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Analytical Endpoints

class EmployeesAverageAgePerIndustry(APIView):
    def get(self, request):
        df = get_df()

        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])

        df = df[df['date_of_birth'].notnull()]
        df = df[df['industry'].notnull()]
        df = df[df['industry'] != '']

        # .astype('<m8[Y]') ignores the month and day of the result
        df['age'] = (pd.Timestamp('now') - df['date_of_birth']).astype('<m8[Y]')

        result = df.groupby('industry')['age'].mean()
        result = result.to_json()

        return Response(json.loads(result), status=status.HTTP_200_OK)


class EmployeesAverageSalaryPerIndustry(APIView):
    def get(self, request):
        df = get_df()

        df = df[df['salary'].notnull()]
        df = df[df['industry'].notnull()]
        df = df[df['industry'] != '']

        result = df.groupby('industry')['salary'].mean()
        result = result.to_json()

        return Response(json.loads(result), status=status.HTTP_200_OK)


class EmployeesAverageSalaryPerYearsOfExperience(APIView):
    def get(self, request):
        df = get_df()

        df = df[df['salary'].notnull()]
        df = df[df['years_of_experience'].notnull()]

        result = df.groupby('years_of_experience')['salary'].mean()
        result = result.to_json()

        return Response(json.loads(result), status=status.HTTP_200_OK)


class EmployeesAverageSalaryPerGender(APIView):
    def get(self, request):
        df = get_df()

        df = df[df['salary'].notnull()]
        df = df[df['gender'].notnull()]

        result = df.groupby('gender')['salary'].mean()
        result = result.to_json()

        return Response(json.loads(result), status=status.HTTP_200_OK)


class EmployeesAverageAgePerGender(APIView):
    def get(self, request):
        df = get_df()

        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])

        df = df[df['date_of_birth'].notnull()]
        df = df[df['gender'].notnull()]

        # .astype('<m8[Y]') ignores the month and day of the result
        df['age'] = (pd.Timestamp('now') - df['date_of_birth']).astype('<m8[Y]')

        result = df.groupby('gender')['age'].mean()
        result = result.to_json()

        return Response(json.loads(result), status=status.HTTP_200_OK)
