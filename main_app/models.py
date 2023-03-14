from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
  url = models.CharField(max_length=200)
  

  def __str__(self):
    return f"Photo for post_id: {self.post_id} @{self.url}"
  
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(max_length=250)
    date = models.DateTimeField()
    photo = models.ForeignKey(Photo, max_length=250)
    

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"
    
