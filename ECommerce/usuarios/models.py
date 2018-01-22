from django.db import models
from django.contrib.auth.models import AbstractUser
 
class CustomUser(AbstractUser):
    pass
 
class LinkedInUser(CustomUser):
    linkedin_id = models.CharField(max_length=30, unique=True, blank=False)
 
    class Meta:
        verbose_name = 'LinkedIn User'