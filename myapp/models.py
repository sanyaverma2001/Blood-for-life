from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField

# Create your models here.


class Info(models.Model):
    Full_Name=models.CharField(max_length=200)

    Phone_number=models.CharField(max_length=12,unique=True)
    Email=models.CharField(max_length=200,unique=True)
    Age=models.CharField(max_length=2)
    Blood_Group=models.CharField(max_length=300)
    Last_donated=models.DateField('XYZ Date')
    Address=models.CharField(max_length=300)
    City=models.CharField(max_length=300)
    Pin_code=models.CharField(max_length=8)
    State=models.CharField(max_length=300)
   