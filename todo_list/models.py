from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField(primary_key=True)
    Mobile = models.CharField(max_length=10, unique=True)
    Password = models.CharField(max_length=15)
    def __str__(self):
        return self.Name



class list(models.Model):
    Email = models.EmailField(default="")
    item = models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    def __str__(self):
        return self.Email + ' | ' +self.item + ' | ' + str(self.completed)

