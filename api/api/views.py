from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .models import Employee
from .paginations import StandardResultsSetPagination
from .serializers import EmployeeSerializer


class EmployeeListView(generics.ListAPIView):
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
        'gender',
        'date_of_birth',
        "industry",
        "salary",
        "years_of_experience"
    ]

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('sort', None)

        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset
