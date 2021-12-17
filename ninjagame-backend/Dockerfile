FROM python:3-slim-buster

WORKDIR /app

COPY ninjagame-backend/requirements.txt ninjagame-backend/requirements.txt
RUN pip3 install -r ninjagame-backend/requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
