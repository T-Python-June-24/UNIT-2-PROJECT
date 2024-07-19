from django.db import models

# Create your models here.


class Activity(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Itinerary(models.Model):
    days = models.IntegerField()
    activities = models.ManyToManyField(Activity)

    def __str__(self):
        return f"Itinerary for {self.days} days"
    


class ItineraryItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.IntegerField()