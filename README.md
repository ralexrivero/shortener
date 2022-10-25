# URL shortener

## Description

This is a simple URL shortener. It uses a hash of the URL as the short URL.

## docker

- `docker build -t py-dj-sh:1.0`

## development environment

- `docker run -d -it --rm -p 8000:8000 -name py-dj-sh-0 -v /home/ralex/code/shortener:/code py-dj-sh:1.0`
- `docker exec -it py-dj-sh-0 sh`
- `python manage.py runserver 0.0.0.0:8000`
