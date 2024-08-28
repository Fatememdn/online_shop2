from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    address = models.TextField(blank=True, null=True)
    def __str__(self) :
        return self.name 


