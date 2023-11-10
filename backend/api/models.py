from django.db import models

# Create your models here.



"""Model Blog."""
class Blog(models.Model):
    
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.body