from django.db import models

# Create your models here.

# Following Django conventions, we'll define a model for each table in our database.
class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    is_cool = models.BooleanField()

    # representation on the database
    def __str__(self):
        return self.name
