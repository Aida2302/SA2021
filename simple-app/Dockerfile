# pull official base image
FROM tiangolo/uwsgi-nginx-flask:python3.6

# set work directory
WORKDIR /usr/src/app

#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN apt-get update
RUN apt-get install --reinstall ca-certificates -y

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN export LDFLAGS="-L/usr/local/opt/openssl/lib"
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . /usr/src/app/
