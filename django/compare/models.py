from django.db import models

class CompareList(models.Model):
    name = models.CharField(max_length=80,unique=True)
    #compared = models.ForeignKey()#TODO

    def __str__(self):
        return self.name

class Result(models.Model):
    size = models.IntegerField()
    winner = models.CharField(max_length=80,unique=True)
    type = models.IntegerField()
    def __str__(self):
        return self.winner
