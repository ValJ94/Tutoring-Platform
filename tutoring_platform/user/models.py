from django.db import models
from django.contrib.auth.models import User

# Create your models here.

maxCharLength = 128

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=maxCharLength)
    middle_name = models.CharField(max_length=maxCharLength, blank=True)
    surname = models.CharField(max_length=maxCharLength)
    age = models.IntegerField()
    description = models.TextField(blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non Binary'),
        ('PNTD', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=4, choices=GENDER_CHOICES, blank=True)
    picture = models.ImageField(upload_to='profilePics', blank=True)


    def __str__(self):
        return self.user.first_name + self.user.last_name