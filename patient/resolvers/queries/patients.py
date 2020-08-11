from typing import Any, Dict, Optional

from ariadne import convert_kwargs_to_snake_case

from patient.models import Patient
from django.db import transaction


class PatientsQueries:
    """
    Methods used to retrieve Patients data
    """

    @staticmethod
    def filter(queryset, filter_input):
        return queryset.filter(**filter_input)

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_patient(_, info, uid):

        try:
            with transaction.atomic():
                return dict(
                    status=True,
                    object=Patient.objects.filter(uid=uid).not_deleted()[0]
                )
        except Exception as e:
            return dict(
                status=False,
                error=f'An error as occurred {e}'
            )

    @staticmethod
    @convert_kwargs_to_snake_case
    def get_patients(_, info, filter_input: Optional[Dict[Any, Any]] = None):

        try:
            if filter_input is not None:
                return dict(status=True,
                        object= PatientsQueries.filter(
                            Patient.objects.all().not_deleted(),
                            filter_input=filter_input))
            else:
                return dict(status=True,
                            object=Patient.objects.all().not_deleted())


        except Exception as e:
            return dict(status=False, error=f"An error as occurred {e}")