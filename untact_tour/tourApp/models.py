from django.db import models

# Create your models here.
class User(models.Model) :
    user_name = models.CharField(max_length=20)
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=12)
    user_email = models.CharField(max_length=20)

    