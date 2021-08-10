from django.conf import settings
from django.utils import timezone
from django.db import models


class Add_Object(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    classe = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def add(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title