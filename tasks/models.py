from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_created', )

    def get_absolute_url(self):
        return reverse('home')

