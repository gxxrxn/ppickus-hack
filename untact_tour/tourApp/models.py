from django.db import models

# Create your models here.
class Users(models.Model) :
    user_name = models.CharField(max_length=20)
    user_id = models.CharField(max_length=10)
    user_pw = models.CharField(max_length=12)
    user_email = models.CharField(max_length=20)

class Categories(models.Model) :
    category_name = models.CharField(max_length=15)
    category_num = models.IntegerField()

class Videos(models.Model) :
    video_name = models.CharField(max_length=80)
    video_num = models.IntegerField()
    video_path = models.CharField(max_length=100)
    thumb_path = models.CharField(max_length=100)
    video_explain = models.CharField(max_length=100)
    pacticipate_category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name='category')
    


