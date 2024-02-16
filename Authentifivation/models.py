from django.db import models

# Create your models here.
class myUser1(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
      #  return self.email
        return self.name

class myUser2(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

