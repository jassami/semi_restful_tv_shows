from time import strptime
from django.db import models
from django.db.models.fields import CharField
from datetime import date, datetime

class ShowManager(models.Manager):
    def basic_validator(self, post_data, curr_title):
        errors={}
        if curr_title != post_data['title']:
            check_title= Show.objects.filter(title= post_data['title'])
            if check_title:
                errors['title_input']= "This show title already exists."
        if len(post_data['title'])< 3:
            errors['title_input']= "Title must be more than 3 charactors long."
        if len(post_data['title'])> 255:
            errors['title_long']= "Title must be less than 255 charactors long."
        if len(post_data['network'])< 2:
            errors['network_input']= "Network must be at least 2 charactors long."
        if len(post_data['description'])> 0 and len(post_data['description'])<10:
            errors['description_input']= "Description must be at least 10 charactors long."
        if len(post_data['release_date']) == 0 or len(post_data['release_date'])< 8:
            errors['release_input'] = "Release date must be mm/dd/yyyy."
        if datetime.strptime(post_data['release_date'], "%Y-%m-%d")> datetime.today():
            errors['release_input']= "Release date must be in the past."
        return errors

class Show(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=45)
    release_date= models.DateField()
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects= ShowManager()
