from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()
    message = models.CharField(max_length = 200)
    data_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('index')