# tify.one

URL shortener

## Description

This is a simple URL shortener. It uses a hash of the URL as the short URL.

https://graphql.org/

https://graphene-python.org/

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

[Graphene](https://docs.graphene-python.org/projects/django/en/latest/installation/#csrf-exempt)

## hash

- using `md5` from `hashlib`

## create url mutation

```graphene
mutation {
  createUrl(fullUrl:"https://google.com") {
    url {
      id
      fullUrl
      urlHash
      clicks
      createdAt
    }
  }
}
```

## query url

```graphene
{
  urls {
    id
    fullUrl
    urlHash
    clicks
    createdAt
    __typename
  }
}
```
