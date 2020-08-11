from ariadne import convert_kwargs_to_snake_case
from patient.models import Patient
from django.db import transaction

class PatientsMutations:
    """
    Mutation methods to perform creation updates and deletion in the Patients model
    """

    def __init__(self):
        pass

    @staticmethod
    def create(_, info, creation_input):

        try:
            with transaction.atomic():

                return dict(
                status=True,
                object=Patient.objects.create(**creation_input)
                )
        except Exception as e:
            return dict(status=False, error=f'An error occurred {e}')

    @staticmethod

    def update(_, info, update_input):

        try:
            with transaction.atomic():
                patient = Patient.objects.get(uid=update_input.get("uid"))
                Patient.objects.filter(uid=update_input.pop("uid")).update(**update_input)
                return dict(
                    status=True,
                    object=patient
                )
        except Exception as e:
            return dict(status=False, error=f'An error occurred {e}')


    @staticmethod

    def soft_delete(_, info, uid):

        try:
            with transaction.atomic():
                record = Patient.objects.get(uid=uid)
                record.soft_delete()
                return dict(
                    status=True,
                    object=record
                )
        except Exception as e:
            return dict(
                status=False,
                error=f'An error occurred: {e}'
            )

    @staticmethod
    @convert_kwargs_to_snake_case
    def activate(_, info, uid):

        try:
            with transaction.atomic():
                record = Patient.objects.get(uid=uid)
                record.activate()
                return dict(
                    status=True,
                    object=record
                )
        except Exception as e:
            return dict(
                status=False,
                error=f'An error occurred: {e}'
            )

    @staticmethod
    @convert_kwargs_to_snake_case
    def deactivate(_, info, uid):

        try:
            with transaction.atomic():
                record = Patient.objects.get(uid=uid)
                record.deactivate()
                return dict(
                    status=True,
                    object=record
                )
        except Exception as e:
            return dict(
                status=False,
                error=f'An error occurred: {e}'
            )