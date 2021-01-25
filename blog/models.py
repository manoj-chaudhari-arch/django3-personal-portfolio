from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    crt = models.DateTimeField()

    def __str__(self):
        return self.name
