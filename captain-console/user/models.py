from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    passhash = models.CharField(max_length=50)
    image = models.CharField(max_length=50, null=True)
    name = models.CharField(max_length=50, null=True)
    searches = models.TextField()
    admin = models.BooleanField()

