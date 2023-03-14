from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    # picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    caption = models.TextField(max_length=250)
    date = models.DateTimeField()

    def __str__(self):
        return f"Photo for post_id: {self.picture_id} @{self.url}"