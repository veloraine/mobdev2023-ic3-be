from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.name
