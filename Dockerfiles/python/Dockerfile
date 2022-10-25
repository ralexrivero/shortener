FROM python:alpine

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
VOLUME /code
