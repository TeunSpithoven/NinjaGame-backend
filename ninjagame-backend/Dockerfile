# FROM python:3-slim-buster

# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# COPY ninjagame-backend/requirements.txt ninjagame-backend/requirements.txt
# RUN pip3 install -r ninjagame-backend/requirements.txt

# COPY . .

# WORKDIR /ninjagame-backend

# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

# EXPOSE 8000

FROM python:3
# Sets an environmental variable that ensures output from python is sent straight to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1
# Sets the container's working directory to /app
WORKDIR /app
# Copies all files from our local project into the container
COPY . .
# runs the pip install command for all packages listed in the requirements.txt file
RUN pip install -r ninjagame-backend-requirements.txt
