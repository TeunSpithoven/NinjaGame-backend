FROM python:3-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# WORKDIR /app/ninjagame-backend

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
