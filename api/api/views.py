from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeList(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
