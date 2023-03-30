from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Employee
from .paginations import StandardResultsSetPagination
from .serializers import EmployeeSerializer


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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeePutView(APIView):
    def put(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeDeleteView(APIView):
    def delete(self, request, id):
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
