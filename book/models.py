from django.db import models
from datetime import datetime 

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=True)
    year = models.IntegerField(default=datetime.now().year)
    
    def __str__(self):
        return self.title
    
    