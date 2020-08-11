import pandas as pd
from patient.models import *
from django.conf import settings
from os.path import join

from django.core.management.base import BaseCommand

def prefill_patients(filename):
    data = pd.read_csv(filename)
    # convert data to a list of dictionaries for easy data entry
    patients_records = data.T.to_dict().values()
    try:
        for record in patients_records:
            Doctor.objects.create(**record)
            print(f'added patients record for {record["last_name"]}')
    except Exception as e:
        print(f"DB prefill process failed due to {e}")


class Command(BaseCommand):

    def handle(self, *args, **options):
        prefill_patients(join(settings.BASE_DIR,'postgres_prefill/patient_list.csv'))