from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    subject =models.CharField(max_length=100)
    comments =models.TextField()

    def __str__(self):
        return self.email

class Contacts(models.Model):
    email = models.EmailField()
    subject =models.CharField(max_length=100)
    comments =models.TextField()

    def __str__(self):
        return self.email