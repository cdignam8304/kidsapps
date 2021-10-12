from django.contrib import admin
from .models import Animal

# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['english', 'french', 'photo']


admin.site.register(Animal, AnimalAdmin)

