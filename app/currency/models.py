from django.db import models


class Rate(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=21)
    salary = models.DecimalField(max_digits=6, decimal_places=2)  # 1234.56
    state = models.CharField(max_length=2)
    # data_r = models.DateTimeField(auto_now_add=True)
    # car = models.CharField(max_length=10)
    child = models.BooleanField(max_length=5)
