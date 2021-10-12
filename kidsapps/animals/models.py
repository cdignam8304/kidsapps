from django.db import models

# Create your models here.

class Animal(models.Model):
    english = models.CharField(max_length=20)
    french = models.CharField(max_length=20)
    photo = models.ImageField(blank=True)

    class Meta:
        ordering = ['english']

    def __str__(self):
        return self.english
