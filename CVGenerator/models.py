from django.db import models

# Create your models here.

class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    prompt = models.TextField()
    education = models.TextField(null=True)
    experience = models.TextField(null=True)
    languages = models.TextField()
    references = models.TextField()

    def __str__(self):
        return self.name
