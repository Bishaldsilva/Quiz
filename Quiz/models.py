from django.db import models

# Create your models here.
class exam(models.Model):
    question = models.CharField(max_length=200)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct = models.CharField(max_length=100)