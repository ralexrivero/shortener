# tify.one

- Shortify one userspace
- tify your way
- Shortify valid urls using sliced md5 hash
- `tify.one/hash` shortified url to redirect
- `tify.one` redirects to `app.tify.one`
- `bad hash` shows `404` page
- `app.tify.one` to access the home page and full functionality
- `blog.tify.one` to access the blog
- `help.tify.one`
- `user.tify.one` the user space shotified profile and urls i.e. `user.tify.one/bio` for general profile or `user.tify.one/ig` for specific custom links

## Services

- Namecheap
- DigitalOcean
- ssl Certbot
- ssh
- datadog
- nginx

## References

- [graphql](https://graphql.org/)
- [graphene](https://graphene-python.org/)
- [django-hosts](https://django-hosts.readthedocs.io/en/latest/)

## docker

- `docker build -t sh-py:1.0 .`

## development environment

- `docker run -d -it --rm -p 8000:8000 --name sh-py-0 -v /home/ralex/code/shortener:/code sh-py:1.0`
- `docker exec -it sh-py-0 sh`
- `python manage.py runserver 0.0.0.0:8000`

## project

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py runserver 0.0.0.0:8000`

## create superuser

- `python manage.py createsuperuser`
- `admin.tify.one`

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
  createUrl(urlFull:"https://ralex.me") {
    url {
      id
      urlFull
      urlHash
      visits
      dateCreated
    }
  }
}
```

## query url

```graphene
query {
  urls{
    id
    urlFull
    urlHash
    visits
    dateCreated
    __typename
  }
}
```

## Docker compose for development

- `docker compose up -d --build`
- if fails
- `docker compose down -v`
- `docker compose exec web python manage.py migrate --noinput`
- `docker compose exec web python manage.py migrate`
- `docker compose exec db psql --username=postgres --dbname=postgres_dev`
- `docker volume inspect tifyone_postgres_data`
- `chmod +x entrypoint.sh`

## Docker compose production

- `docker compose -f docker-compose.prod.yaml up -d --build`

- `docker compose -f docker-compose.prod.yaml down -v`
- `docker compose -f docker-compose.prod.yaml up -d --build`
- `docker compose -f docker-compose.prod.yaml exec web python manage.py migrate --noinput`

- `docker compose logs -f`

- `docker compose exec web python manage.py flush --no-input`
- `docker compose exec web python manage.py migrate`

### build and run the production environment

- `docker compose -f docker-compose.prod.yaml up -d --build`
- `docker compose -f docker-compose.prod.yaml exec web python manage.py migrate --noinput`

- `docker compose -f docker-compose.prod.yaml down -v`
- `docker compose -f docker-compose.prod.yaml up -d --build`
- `docker compose -f docker-compose.prod.yaml exec web python manage.py migrate --noinput`
