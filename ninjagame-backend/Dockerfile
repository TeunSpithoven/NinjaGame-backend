FROM python:3-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app
WORKDIR /ninjagame-backend

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .


CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
