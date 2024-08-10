from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name