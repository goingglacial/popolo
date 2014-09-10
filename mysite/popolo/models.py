from django.db import models

class Pops (models.Model):
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=10)
    pop = models.CharField(max_length=40)