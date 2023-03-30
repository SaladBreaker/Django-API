from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from api.models import Employee

from api.views import update_df


class AnalyticalAverageAgePerIndustryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Employee.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",  # 33
            industry="IT",
            salary=50000.0,
            years_of_experience=3.0,
        )

        self.employee_2 = Employee.objects.create(
            id=2,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1991-01-01",  # 32
            industry="IT",
            salary=50000.0,
            years_of_experience=3.0,
        )

        self.employee_3 = Employee.objects.create(
            id=3,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1992-01-01",  # 31
            industry="IT",
            salary=50000.0,
            years_of_experience=3.0,
        )
        update_df()

    def test_base_case(self):
        response = self.client.get(reverse("employees-average-age-per-industry"))

        self.assertEqual(response.data["IT"], 32)


class AnalyticalAverageSalaryPerIndustryTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Employee.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",  # 33
            industry="IT",
            salary=40000.0,
            years_of_experience=3.0,
        )

        self.employee_2 = Employee.objects.create(
            id=2,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1991-01-01",  # 32
            industry="IT",
            salary=50000.0,
            years_of_experience=3.0,
        )

        self.employee_3 = Employee.objects.create(
            id=3,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1992-01-01",  # 31
            industry="IT",
            salary=60000.0,
            years_of_experience=3.0,
        )
        update_df()

    def test_base_case(self):
        response = self.client.get(reverse("employees-average-salary-per-industry"))

        self.assertEqual(response.data["IT"], 50000)


class AnalyticalAverageSalaryPerYearsOfExperience(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Employee.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",  # 33
            industry="IT",
            salary=40000.0,
            years_of_experience=4.0,
        )

        self.employee_2 = Employee.objects.create(
            id=2,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1991-01-01",  # 32
            industry="IT",
            salary=50000.0,
            years_of_experience=4.0,
        )

        self.employee_3 = Employee.objects.create(
            id=3,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1992-01-01",  # 31
            industry="IT",
            salary=60000.0,
            years_of_experience=4.0,
        )
        update_df()

    def test_base_case(self):
        response = self.client.get(
            reverse("employees-average-salary-per-years-of-experience")
        )

        self.assertEqual(response.data["4.0"], 50000)


class AnalyticalAverageSalaryPerGender(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Employee.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",  # 33
            industry="IT",
            salary=40000.0,
            years_of_experience=3.0,
        )

        self.employee_2 = Employee.objects.create(
            id=2,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1991-01-01",  # 32
            industry="IT",
            salary=50000.0,
            years_of_experience=4.0,
        )

        self.employee_3 = Employee.objects.create(
            id=3,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1992-01-01",  # 31
            industry="IT",
            salary=60000.0,
            years_of_experience=5.0,
        )
        update_df()

    def test_base_case(self):
        response = self.client.get(reverse("employees-average-salary-per-gender"))

        self.assertEqual(response.data["Male"], 50000)


class AnalyticalAverageAgePerGender(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Employee.objects.create(
            id=1,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1990-01-01",  # 33
            industry="IT",
            salary=40000.0,
            years_of_experience=3.0,
        )

        self.employee_2 = Employee.objects.create(
            id=2,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1991-01-01",  # 32
            industry="IT",
            salary=50000.0,
            years_of_experience=4.0,
        )

        self.employee_3 = Employee.objects.create(
            id=3,
            first_name="John",
            last_name="Doe",
            email="john@example.com",
            gender="Male",
            date_of_birth="1992-01-01",  # 31
            industry="IT",
            salary=60000.0,
            years_of_experience=5.0,
        )
        update_df()

    def test_base_case(self):
        response = self.client.get(reverse("employees-average-age-per-gender"))

        self.assertEqual(response.data["Male"], 32)
