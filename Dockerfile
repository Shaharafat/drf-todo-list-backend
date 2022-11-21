# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster
WORKDIR /server
COPY requirements.txt /server 
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
