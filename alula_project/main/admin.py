from django.contrib import admin
from .models import HeritageSite, NatureActivity, Event, Accommodation, Dining, Amenity, AccommodationImage, DiningImage

admin.site.register(HeritageSite)
admin.site.register(NatureActivity)
admin.site.register(Event)
admin.site.register(Amenity)

class AccommodationImageInline(admin.TabularInline):
    model = AccommodationImage
    extra = 1

class AccommodationAdmin(admin.ModelAdmin):
    inlines = [AccommodationImageInline]

admin.site.register(Accommodation, AccommodationAdmin)
############################

class DiningImageInline(admin.TabularInline):
    model = DiningImage
    extra = 1

class DiningAdmin(admin.ModelAdmin):
    inlines = [DiningImageInline]

admin.site.register(Dining, DiningAdmin)
