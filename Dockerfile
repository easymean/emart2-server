#./Dockerfile
FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app/emart2-server

## Install packages
COPY requirements.txt ./
RUN pip3 install --upgrade pip3
RUN pip3 install -r requirements.txt
RUN ./src/manage.py collectstatic --noinput

## Copy all src files
COPY emart2-server .

## Run the application on the port 8080
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
