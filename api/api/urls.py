"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import (
    EmployeeListView,
    EmployeeGetView,
    EmployeePostView,
    EmployeePutView,
    EmployeeDeleteView, EmployeesAverageAgePerIndustry, EmployeesAverageSalaryPerIndustry,
    EmployeesAverageSalaryPerYearsOfExperience, EmployeesAverageSalaryPerGender, EmployeesAverageAgePerGender,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # Employee
    path("employees/", EmployeeListView.as_view(), name="employees-list"),
    path("employees/<int:id>/", EmployeeGetView.as_view(), name="employees-get"),
    path(
        "employees/create/",
        EmployeePostView.as_view(http_method_names=["post"]),
        name="employees-create",
    ),
    path(
        "employees/<int:id>/update/",
        EmployeePutView.as_view(http_method_names=["put"]),
        name="employees-update",
    ),
    path(
        "employees/<int:id>/delete/",
        EmployeeDeleteView.as_view(http_method_names=["delete"]),
        name="employees-delete",
    ),

    # Analytical Endpoints
    path(
        "analytical/employees-average-age-per-industry",
        EmployeesAverageAgePerIndustry.as_view(),
        name="employees-average-age-per-industry"
    ),
    path(
        "analytical/employees-average-salary-per-industry",
        EmployeesAverageSalaryPerIndustry.as_view(),
        name="employees-average-salary-per-industry"
    ),
    path(
        "analytical/employees-average-salary-per-years-of-experience",
        EmployeesAverageSalaryPerYearsOfExperience.as_view(),
        name="employees-average-salary-per-years-of-experience"
    ),
    path(
        "analytical/employees-average-salary-per-gender",
        EmployeesAverageSalaryPerGender.as_view(),
        name="employees-average-salary-per-gender"
    ),
    path(
        "analytical/employees-average-age-per-gender",
        EmployeesAverageAgePerGender.as_view(),
        name="employees-average-age-per-gender"
    )
]
