FROM python:3-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ninjagame-backend/requirements.txt ninjagame-backend/requirements.txt
RUN cd /ninjagame-backend && pip3 install -r requirements.txt

COPY . .

RUN cd /ninjagame-backend && python3 manage.py runserver 0.0.0.0:8000

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

EXPOSE 8000
