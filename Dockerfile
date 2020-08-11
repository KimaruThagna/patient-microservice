FROM python:3.8.3-alpine

ENV MICRO_SERVICE=/home/app/microservice
ENV APP_USER=app_user
# create the app user
RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
# set work directory


RUN mkdir -p $MICRO_SERVICE
RUN mkdir -p $MICRO_SERVICE/static

# where our code lives
WORKDIR $MICRO_SERVICE

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++
# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . $MICRO_SERVICE
RUN pip install -r requirements.txt
COPY ./entrypoint.sh $MICRO_SERVICE

# chown all the files to the app user
RUN chown -R $APP_USER:$APP_USER $MICRO_SERVICE

# change to the app user
USER $APP_USER

CMD ["/bin/bash", "/home/app/microservice/entrypoint.sh"]
#ENTRYPOINT["entrypoint.sh"]
