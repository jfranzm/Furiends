from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
TYPE = (
   (1, 'Profile'),
   (2, 'Pets')
)

class Photo(models.Model):
  url = models.CharField(max_length=200)
  caption = models.CharField(max_length=250)
  category = models.IntegerField(choices=TYPE)
  date = models.DateField(default = date.today)
  likes = models.BigIntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for post_id: {self.caption} with {self.likes} uploaded on {self.date} by user {self.user}"
  

class Post(models.Model):
    caption = models.TextField(max_length=250)
    date = models.DateField(default = date.today) 
    likes = models.BigIntegerField()   
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for post_id: {self.caption} created by user {self.user} on {self.date}"
    
