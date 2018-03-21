from django.db import models
from schools.models import Kindergarten

class CompareList(models.Model):
    Kindergarten = Kindergarten
    rating = models.IntegerField()
    #compared = models.ForeignKey()#TODO

    def __str__(self):
        return self.name
