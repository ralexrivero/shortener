# URL shortener

## Description

This is a simple URL shortener. It uses a hash of the URL as the short URL.

## docker

- `docker build -t sh-py:1.0 .`

## development environment

- `docker run -d -it --rm -p 8000:8000 --name sh-py-0 -v /home/ralex/code/shortener:/code sh-py:1.0`
- `docker exec -it sh-py-0 sh`
- `python manage.py runserver 0.0.0.0:8000`

## project

- `python manage.py migrate`

## graphql

- add to `settings.py` the Schema for for all objects types

```python
GRAPHENE = {
    'SCHEMA': 'shortener.schema.schema'
}
```

## hash

- using `md5` from `hashlib`

