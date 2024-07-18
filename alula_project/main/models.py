from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

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


class Dining(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default='Fine dining')
    cuisine = models.CharField(max_length=100)
    price = models.CharField(max_length=100, default='$$')
    dress = models.CharField(max_length=100, default='Smart casual')
    phone = PhoneNumberField(default = '+966 503782355')
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class DiningImage(models.Model):
    dining = models.ForeignKey(Dining, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='dining_images')

    def __str__(self):
        return f"Image for {self.dining.name}"

class Amenity(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Accommodation(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=100)
    phone = PhoneNumberField(default = '+966 503782355')
    location = models.CharField(max_length=200)
    amenities = models.ManyToManyField(Amenity)

    def __str__(self):
        return self.name

class AccommodationImage(models.Model):
    accommodation = models.ForeignKey(Accommodation, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accommodation_images')

    def __str__(self):
        return f"Image for {self.accommodation.name}"
