FROM ubuntu:20.04
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get -y update && apt install python3 python3-pip -y
RUN pip3 install --upgrade pip
RUN pip3 install Django
WORKDIR /usr/src/app
COPY . /usr/src/app
WORKDIR mysite
EXPOSE 5000
CMD [ "python3", "./manage.py", "runserver", "0.0.0.0:5000" ]
