from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=20)


    def __str__(self):
        return self.name + ' ' + self.email