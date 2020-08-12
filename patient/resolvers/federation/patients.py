from ariadne.contrib.federation import FederatedObjectType

from patient.models import Patient

patient_federated_object = FederatedObjectType("Patient")


@patient_federated_object.resolve_reference
def get_patient_by_uid(representation):
    return Patient.objects.get(patient_number=representation.get("patient_number"))


@patient_federated_object.field("uid")
def resolve_id(obj, *_):
    return obj.uid


@patient_federated_object.field("indexingId")
def resolve_indexing_id(obj, *_):
    return obj.indexing_id


@patient_federated_object.field("first_name")
def resolve_first_name(obj, *_):
    return obj.first_name

@patient_federated_object.field("last_name")
def resolve_last_name(obj, *_):
    return obj.last_name

@patient_federated_object.field("patient_number")
def resolve_patient_number(obj, *_):
    return obj.patient_number

@patient_federated_object.field("county")
def resolve_county(obj, *_):
    return obj.county
