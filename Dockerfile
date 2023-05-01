FROM python:3.10

WORKDIR /app/web_rz

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/web_rz

