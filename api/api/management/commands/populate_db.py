import pandas as pd
import numpy as np

from django.core.management.base import BaseCommand

from api.models import Employee

DATA_FILE = "api/management/commands/db_data/initial_data.json"


class Command(BaseCommand):
    help = "Populate the DB  with the initial employee data."

    def handle(self, *args, **options):
        with open(DATA_FILE, "r") as f:
            data_json = f.read()

        df = pd.read_json(data_json)

        df["date_of_birth"] = pd.to_datetime(df["date_of_birth"])
        df = df.replace(["NaN", "n/a"], [None, None])
        df = df.replace(np.nan, None, regex=True)

        for index, row in df.iterrows():
            Employee(
                id=row["id"],
                first_name=row["first_name"],
                last_name=row["last_name"],
                email=row["email"],
                gender=row["gender"],
                date_of_birth=row["date_of_birth"],
                industry=row["industry"],
                salary=row["salary"],
                years_of_experience=row["years_of_experience"],
            ).save()
