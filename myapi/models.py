from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female'),),default='F')
    def __str__(self):
        return self.name
