from django.db import models
from core.validators import email_validator



class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,validators=[email_validator])
    subject=models.CharField(max_length=200)
    message=models.TextField()

    def __str__(self) :
        return self.name
    