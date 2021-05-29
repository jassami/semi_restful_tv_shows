from django.db import models
from django.db.models.fields import CharField

class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=45)
    release_date= models.DateTimeField()
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)