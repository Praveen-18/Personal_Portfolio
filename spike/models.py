from django.db import models

# Create your models here.

class contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    comments = models.TextField()

    def __str__(self):
        return self.name