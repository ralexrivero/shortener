from django.db import models
from hashlib import md5

class Url(models.Model):
    url_full = models.URLField(unique=True)
    url_hash = models.URLField(unique=True)
    visits = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def visited(self):
        self.visits += 1
        self.save()

    def save(self, *args, **kwargs):
        if not self.id:
            self.url_hash = md5(self.full_url.encode()).hexdigest()[:9]

        return super().save(*args, **kwargs)
