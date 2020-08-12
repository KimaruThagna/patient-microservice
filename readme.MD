## Patient Service Micro Django
Part 2 of a journey through building a django-graphql based micro service.
The repo also explores using [ariadne](https://ariadnegraphql.org/) to build a federated schema.
This is part of a micro service architecture where this handles the patient's service. Other services in this project are the `Doctors` and `diagnosis` services.
## Tech stack
1. [Django](https://www.djangoproject.com/) for backend and business logic
2. [Ariadne](https://ariadnegraphql.org/) to resolve python/django objects to graphql API
3. [Docker](https://docs.docker.com/get-docker/) and
 [Docker compose](https://docs.docker.com/compose/) for container management and deployment.
4. [Gunicorn](https://gunicorn.org/) To serve Django in a production state
5. [Nginx](https://www.nginx.com/) To act as a reverse proxy for Gunicorn.
 
## Overall Architecture.
**Micro-django 2** is modelled as a patient's service app. The whole architecture involves 3 micro services
1. [Doctors service](https://github.com/KimaruThagna/micro-django) part 1
2. [Patient's service](https://github.com/KimaruThagna/patient-microservice) part 2
3. [Diagnosis service](https://github.com/KimaruThagna/diagnosis-microservice) part 3

and a final service running [apollo federation](https://www.apollographql.com/docs/apollo-server/federation/introduction/) that allows a client to access all 3 services
via a single data graph by implementing a [gateway](https://www.apollographql.com/docs/apollo-server/federation/gateway/).
The gateway service repo can be found [here](https://github.com/KimaruThagna/hospital-federated)

## Installation and running
A pre requisite to install and run this service is 
having [docker]() and [docker compose]() installed
Once installed, clone this repo into your local machine  and copy the contents of `example.env` into your own `.env` file. 
Change the variables as need be

Navigate to the position of the `docker-compose.yml` file
To spin up the service, run the command
```apex
docker-compose up
```
To access the service via the broswer, log on to [http://0.0.0.0:1338/]() since we are serving the app via NGINX

To view the app from the admin side, access the admin via the url [http://0.0.0.0:1338/admin]() and log in with the superuser credentials created in the `.env` file

## Sample Query
- `get_patients`
```
{
  patients
  {
    status
    object{
      patient_number
      first_name
      uid
      last_name
    }
  }
}
```
- `get_patient`  use whichever uid will be amongst those retrieved in the first query.
```
{
  patient(uid:"f6fea0be-20ff-4c12-b0cb-fb32d5512346")
  {
    status
    object
    {
      first_name
      last_name
      patient_number
    }
  }
}
```

## Sample mutation
- ``create_patient``
```
mutation
{
createPatient{
first_name:"John"
last_name:"Doe"
patient_number:"001265789" 
county:"Lamu"
}
status
object
{
uid
last_name
first_name
county
}
}


```

-   `update_patient`

```
mutation
{
updatePatient{
uid:"f6fea0be-20ff-4c12-b0cb-fb32d5512346"
county:"Lamu"
}
status
object
{
uid
first_name
last_name
county
}
}

```

- `delete_patient`
```
mutation
{
  deletePatient(uid:"f3dc4b5e-000-4b88-82a9-345eed624511")
  {
    status
  }
}
```
- `activate_patient`
```
mutation
{
  activatePatient(uid:"f3dc4b5e-111-d455-82a9-345eed624511")
  {
    status
  }
}
```
