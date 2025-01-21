from django.db import models

# Create your models here.
class Database(models.Model):
    FirstName=models.CharField(max_length=30)
    LastName=models.CharField(max_length=30)
    Email_id=models.EmailField(max_length=50)
    Phone_No=models.IntegerField()
    Message=models.TextField(max_length=200)