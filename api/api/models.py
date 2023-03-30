from django.db import models


class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=10, null=True)
    date_of_birth = models.DateField()
    industry = models.CharField(max_length=300, null=True)
    salary = models.FloatField()
    years_of_experience = models.FloatField()

    others = models.JSONField(default=dict, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
