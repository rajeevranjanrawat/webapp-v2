from django.contrib import admin
from .models import Photo
# Register your models here.

class Photoadmin(admin.ModelAdmin):

    list_display = ["title", "timestamp"]

    class Meta:

        model = Photo

admin.site.register(Photo, Photoadmin)