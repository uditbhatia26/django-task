from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=20)
    file = models.FileField(upload_to='uploads/', null=True, blank=True)


    def __str__(self):
        return self.name + ' ' + self.email