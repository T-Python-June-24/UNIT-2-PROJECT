from django.db import models

class HeritageSite(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    images = models.ImageField(upload_to='heritage_images')

    def __str__(self):
        return self.name

class NatureActivity(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    difficulty_level = models.CharField(max_length=50)
    images = models.ImageField(upload_to='nature_images')

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    location = models.CharField(max_length=200)
    images = models.ImageField(upload_to='event_images')
    ticket_info = models.TextField()

    def __str__(self):
        return self.name

class Accommodation(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    amenities = models.TextField()
    images = models.ImageField(upload_to='accommodation_images')

    def __str__(self):
        return self.name

class Dining(models.Model):
    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    images = models.ImageField(upload_to='dining_images')
    menu = models.TextField()

    def __str__(self):
        return self.name
