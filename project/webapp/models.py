from django.db import models

# Create your models here.
class Flight(models.Model):
    f_no = models.CharField(max_length=9)
    a_type = models.CharField(max_length=5)
    a_from = models.CharField(max_length=3)
    a_time = models.CharField(max_length=5)
    d_to =  models.CharField(max_length=3)
    d_time = models.CharField(max_length=5)

    def __str__(self):
        return self.f_no
