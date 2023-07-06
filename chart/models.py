from unicodedata import category
from django.db import models

# Create your models here.

class data(models.Model):
    # how_many_days = models.CharField(max_length=200)
    which_day =models.CharField(max_length=20, null=False, blank=False)
    tasks = models.CharField(max_length=200, null=False, blank=False)
    happiness_score = models.FloatField()

    def __str__(self):
        return f'{self.which_day}-{self.happiness_score}-{self.tasks}' 


class analysis(models.Model):
    analysis_day= models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return f'{self.analysis_day}' 
