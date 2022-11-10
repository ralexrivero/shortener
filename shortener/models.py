from django.db import models
from hashlib import md5
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from graphql import GraphQLError


class Url(models.Model):
    url_full = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    visits = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def visited(self):
        self.visits += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.url_full.encode()).hexdigest()[:9]

        validate = URLValidator()
        try:
            validate(self.url_full)
        except ValidationError as e:
            raise GraphQLError('invalid url')

        return super().save(*args, **kwargs)
