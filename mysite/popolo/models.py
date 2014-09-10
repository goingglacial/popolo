from django.db import models

class Popul (models.Model):
    city = models.CharField(max_length=40, primary_key=True)
    state = models.CharField(max_length=10)
    pop = models.CharField(max_length=40)

    def __unicode__(self):
        return self.city
    def __unicode__(self):
        return self.state
    def __unicode__(self):
        return self.pop