from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    fee = models.IntegerField()
    rating = models.FloatField()
    years_experience = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.speciality})"
