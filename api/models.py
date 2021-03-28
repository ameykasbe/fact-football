from django.db import models


class Fact(models.Model):
    content = models.TextField()
