from django.db import models

from utils.base_models import BaseModel


class Patient (BaseModel):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    patient_number = models.CharField(max_length=30, unique=True)
    county = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'