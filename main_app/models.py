from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
TYPE = (
   (1, 'Profile'),
   (2, 'Pets')
)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  caption = models.CharField(max_length=250)
  category = models.IntegerField(choices=TYPE)
  date = models.DateTimeField(default=datetime.now())
  likes = models.BigIntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for post_id: {self.caption} with {self.likes} uploaded on {self.date} by user {self.user}"
  

class Post(models.Model):
    caption = models.TextField(max_length=250)
    date = models.DateTimeField(default=datetime.now())
    likes = models.BigIntegerField()   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for post_id: {self.caption} created by user {self.user} on {self.date}"
    
class Post_User(models.Model):
   user_id = models.BigIntegerField()
   post_id = models.BigIntegerField()

   def __str__(self):
      return f'Foreign key between user_id {self.user_id} and post_id {self.post_id}'
     
    
