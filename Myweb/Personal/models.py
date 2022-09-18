
from django.db import models


# Create your forms here.

class Contactmessage(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    message=models.TextField()
    email = models.EmailField(max_length=100)
    def __str__(self):
        return self.first_name


