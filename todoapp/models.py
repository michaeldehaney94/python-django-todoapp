from django.db import models
import datetime


# Create your models here.
class Task(models.Model):
    # __str__ displays or returns the name of the data in database admin tool instead of the 'object'
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    priority = models.IntegerField()
    date = models.DateField(default=datetime.date.today)
