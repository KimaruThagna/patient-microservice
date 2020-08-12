from ariadne import MutationType, QueryType, gql, load_schema_from_path
from ariadne.contrib.federation import make_federated_schema
from os.path import dirname, join

from patient.resolvers.mutations.patients import *
from patient.resolvers.queries.patients import *

def load_typedef_from_schema():
    type_def = load_schema_from_path(join(dirname(dirname(__file__)), "./gql"))
    type_defs = gql(type_def)
    return type_defs


# query type and its fields resolvers
def bind_query_type_to_resolvers():
    query = QueryType()
    query.set_field("patient", PatientsQueries.get_patient)
    query.set_field("patients", PatientsQueries.get_patients)
    return query

def bind_mutation_type_to_resolvers():
    mutation = MutationType()
    mutation.set_field("createPatient", PatientsMutations.create)
    mutation.set_field("updatePatient", PatientsMutations.update)
    mutation.set_field("deletePatient", PatientsMutations.soft_delete)
    mutation.set_field("activatePatient", PatientsMutations.activate)
    mutation.set_field("deactivatePatient", PatientsMutations.deactivate)
    return mutation


# generate federated schema from type definitions, query, mutations and other objects
def generate_schema():
    type_defs = load_typedef_from_schema()
    query = bind_query_type_to_resolvers()
    mutation = bind_mutation_type_to_resolvers()
    schema = make_federated_schema(type_defs, [query, mutation])
    return schema


# expose schema for imports from other modules
schema = generate_schema()
