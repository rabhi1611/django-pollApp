from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=150)
    option_1 = models.CharField(max_length=30)
    option_2 = models.CharField(max_length=30)
    option_3 = models.CharField(max_length=30)

    option_1_count = models.IntegerField(default=0)
    option_2_count = models.IntegerField(default=0)
    option_3_count = models.IntegerField(default=0)

    def __str__(self):
        return self.question
    
    def total(self):
        return self.option_1_count + self.option_2_count + self.option_3_count