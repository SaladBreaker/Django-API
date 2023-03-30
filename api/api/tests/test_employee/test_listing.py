from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from api.models import Employee


class EmployeeSoringTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Employee.objects.create(
            id=1,
            first_name='John', last_name='Doe', email='john@example.com',
            gender='Male', date_of_birth='1990-01-01', industry='IT',
            salary=50000.0,
            years_of_experience=3.0)
        self.employee_2 = Employee.objects.create(
            id=2,
            first_name='Jane', last_name='Doe', email='jane@example.com',
            gender='Female', date_of_birth='1991-01-01', industry='Marketing', salary=60000.0,
            years_of_experience=5.0)
        self.employee_3 = Employee.objects.create(
            id=3,
            first_name='James', last_name='Smith', email='james@example.com',
            gender='Male', date_of_birth='1992-01-01', industry='Sales', salary=70000.0,
            years_of_experience=10.0)

    def test_by_salary_asc(self):
        response = self.client.get(reverse('employee-list') + '?sort=salary')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['id'], 1)
        self.assertEqual(response.data[1]['id'], 2)
        self.assertEqual(response.data[2]['id'], 3)

    def test_by_salary_desc(self):
        response = self.client.get(reverse('employee-list') + '?sort=-salary')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['id'], 3)
        self.assertEqual(response.data[1]['id'], 2)
        self.assertEqual(response.data[2]['id'], 1)

    def test_by_date_of_birth_asc(self):
        response = self.client.get(reverse('employee-list') + '?sort=date_of_birth')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['id'], 1)
        self.assertEqual(response.data[1]['id'], 2)
        self.assertEqual(response.data[2]['id'], 3)

    def test_by_date_of_birth_desc(self):
        response = self.client.get(reverse('employee-list') + '?sort=-date_of_birth')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 3)
        self.assertEqual(response.data[0]['id'], 3)
        self.assertEqual(response.data[1]['id'], 2)
        self.assertEqual(response.data[2]['id'], 1)


class EmployeeFilteringTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Employee.objects.create(
            id=1,
            first_name='John', last_name='Doe', email='john@example.com',
            gender='Male', date_of_birth='1990-01-01', industry='IT',
            salary=50000.0,
            years_of_experience=3.0)
        self.employee_2 = Employee.objects.create(
            id=2,
            first_name='Jane', last_name='Doe', email='jane@example.com',
            gender='Female', date_of_birth='1991-01-01', industry='Marketing', salary=60000.0,
            years_of_experience=5.0)
        self.employee_3 = Employee.objects.create(
            id=3,
            first_name='James', last_name='Smith', email='james@example.com',
            gender='Male', date_of_birth='1992-01-01', industry='Sales', salary=60000.0,
            years_of_experience=10.0)

    def test_filter_by_first_name(self):
        response = self.client.get(reverse('employee-list') + f'?first_name={self.employee_1.first_name}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], self.employee_1.first_name)

        response = self.client.get(reverse('employee-list') + f'?first_name={self.employee_2.first_name}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], self.employee_2.first_name)

    def test_filter_by_salary(self):
        response = self.client.get(reverse('employee-list') + f'?salary={self.employee_1.salary}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['salary'], self.employee_1.salary)

        response = self.client.get(reverse('employee-list') + f'?salary={self.employee_2.salary}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['salary'], self.employee_2.salary)
        self.assertEqual(response.data[1]['salary'], self.employee_3.salary)


class EmployeePaginationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.employee_1 = Employee.objects.create(
            id=1,
            first_name='John', last_name='Doe', email='john@example.com',
            gender='Male', date_of_birth='1990-01-01', industry='IT',
            salary=50000.0,
            years_of_experience=3.0)
        self.employee_2 = Employee.objects.create(
            id=2,
            first_name='Jane', last_name='Doe', email='jane@example.com',
            gender='Female', date_of_birth='1991-01-01', industry='Marketing', salary=60000.0,
            years_of_experience=5.0)
        self.employee_3 = Employee.objects.create(
            id=3,
            first_name='James', last_name='Smith', email='james@example.com',
            gender='Male', date_of_birth='1992-01-01', industry='Sales', salary=60000.0,
            years_of_experience=10.0)

    def test_with_one_page_size(self):
        response = self.client.get(reverse('employee-list') + f'?page=1&page_size=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], self.employee_1.first_name)

        response = self.client.get(reverse('employee-list') + f'?page=2&page_size=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], self.employee_2.first_name)

        response = self.client.get(reverse('employee-list') + f'?page=3&page_size=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response.data = response.data["results"]
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['first_name'], self.employee_3.first_name)
