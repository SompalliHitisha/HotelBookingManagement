from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Admin(models.Model):
    id: models.AutoField(primary_key=True)
    username = models.CharField(max_length=30,blank=False,unique=True)
    password = models.CharField(max_length=12,blank=False)
    class Meta:
        db_table = "HMadmin_table"
class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,blank=False)
    address=models.CharField(max_length=30,blank=False)
    email=models.CharField(max_length=25,blank=False,unique=True)
    phno=models.CharField(max_length=15,blank=False,unique=True)
    username=models.CharField(max_length=30,blank=False,unique=True)
    password=models.CharField(max_length=12,blank=False)
    class Meta:
        db_table="register_table"


from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    # Add more fields as needed

    def __str__(self):
        return self.name

# forms.py
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

