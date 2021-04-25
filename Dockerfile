#./Dockerfile
FROM python:3

RUN mkdir /srv/emart2-server
WORKDIR /srv/emart2-server

## Install packages
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

## Copy all src files
COPY . .

## Run the application on the port 8080
EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "src.config.wsgi:application"]
