# import the standard Django Model
# from built-in library
from django.db import models

# declare a new model with a name FinnModel


class FinnModel(models.Model):
    # fields of the model

    title=models.CharField(max_length=100)
    description=models.CharField(max_length=100)

    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title


