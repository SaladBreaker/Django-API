from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from api.models import Employee

from api.serializers import EmployeeSerializer


class EmployeeGetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee = Employee.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",
            industry="IT",
            salary=50000.0,
            years_of_experience=3.0,
        )

    def test_when_user_exists(self):
        response = self.client.get(
            reverse("employees-get", kwargs={"id": self.employee.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data, EmployeeSerializer(self.employee).data)

    def test_when_user_does_not_exists(self):
        id = self.employee.id
        self.employee.delete()

        response = self.client.get(reverse("employees-get", kwargs={"id": id}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class EmployeeCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee = Employee(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",
            industry="IT",
            salary=50000.0,
            years_of_experience=3.0,
        )

    def test_when_user_does_not_exists(self):
        response = self.client.post(
            reverse("employees-create"),
            data=EmployeeSerializer(self.employee).data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_when_user_exists(self):
        self.employee.save()

        response = self.client.post(
            reverse("employees-create"),
            data=EmployeeSerializer(self.employee).data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class EmployeeUpdateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee = Employee.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",
            industry="IT",
            salary=50000.0,
            years_of_experience=3.0,
        )

    def test_when_user_exists(self):
        self.employee.industry = "Farming"
        response = self.client.put(
            reverse("employees-update", kwargs={"id": self.employee.id}),
            data=EmployeeSerializer(self.employee).data,
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        serialized_data = EmployeeSerializer(self.employee).data
        del response.data["updated_at"]
        del serialized_data["updated_at"]

        self.assertEqual(response.data, serialized_data)

    def test_when_user_does_not_exist(self):
        self.employee.industry = "Farming"
        response = self.client.put(
            reverse("employees-update", kwargs={"id": self.employee.id}),
            data=EmployeeSerializer(self.employee).data,
            format="json",
        )

        serialized_data = EmployeeSerializer(self.employee).data
        del response.data["updated_at"]
        del serialized_data["updated_at"]

        self.assertEqual(response.data, serialized_data)


class EmployeeUpdateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee = Employee.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",
            industry="IT",
            salary=50000.0,
            years_of_experience=3.0,
        )

    def test_when_user_exists(self):
        response = self.client.delete(
            reverse("employees-delete", kwargs={"id": self.employee.id}),
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_when_user_does_not_exist(self):
        id = self.employee.id
        self.employee.delete()
        response = self.client.delete(
            reverse("employees-delete", kwargs={"id": id}),
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
