from django.db import models

# Create your models here.

class PublicMessage(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True, null= True, blank=True)
    def __str__(self):
        return f'{self.email}'
