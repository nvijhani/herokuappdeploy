from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Suggestions(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    suggestions = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
    
   