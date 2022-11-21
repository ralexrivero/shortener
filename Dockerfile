FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/code
WORKDIR /usr/src/code

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /usr/src/code

EXPOSE 8000

# CMD ["gunicorn", "--chdir", "tify.one", "--bind", ":8000", "tify.wsgi:application"]
