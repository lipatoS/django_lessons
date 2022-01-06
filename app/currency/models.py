from django.db import models
from currency import model_choises as MCH


class SourceModel(models.Model):
    name = models.CharField(max_length=24)


class Rate(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=21)
    salary = models.DecimalField(max_digits=6, decimal_places=2)  # 1234.56
    state = models.CharField(max_length=2)
    date = models.DateTimeField(auto_now_add=True)
    # car = models.CharField(max_length=10)
    child = models.BooleanField(max_length=5)


class ContactUs(models.Model):
    email_to = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.CharField(max_length=2056)
    date = models.DateTimeField(auto_now_add=True)


class Rate2(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    # source = models.CharField(max_length=16)
    source = models.ForeignKey(SourceModel, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=3, choices=MCH.RATE2_TYPES)


class ResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    statuscode = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=256)
    responsetime = models.PositiveSmallIntegerField()
