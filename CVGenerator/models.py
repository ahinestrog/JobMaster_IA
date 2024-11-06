from django.db import models

# Create your models here.

class CV(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    education = models.TextField(null=True)
    experience = models.TextField(null=True)
    languages = models.TextField()
    references = models.TextField()
    prompt = models.TextField()

    def __str__(self):
        return self.name
    
class CVInfo(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.EmailField()
    jobTitle = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    experienceOptions = [
        ("Menos de un año", "Menos de un año"),
        ("1 a 3 años", "1 a 3 años"),
        ("4 a 6 años", "4 a 6 años"),
        ("7 a 10 años", "7 a 10 años"),
        ("Más de 10 años", "Más de 10 años"),
    ]

    experienceYears = models.CharField(max_length=20, choices=experienceOptions)

    def __str__(self):
        return self.jobTitle
