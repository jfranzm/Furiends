from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.TextField(max_length=250)
    date = models.DateTimeField()

    def __str__(self):
        return f"Photo for post_id: {self.post_id} @{self.url}"
    
class Photo(models.Model):
  url = models.CharField(max_length=200)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for post_id: {self.post_id} @{self.url}"