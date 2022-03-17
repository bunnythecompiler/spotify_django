from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone 

class SpotMusic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    song_author = models.CharField(max_length=50,default="user1")
    song_title = models.CharField(max_length=50)
    song_image = models.FileField(upload_to='spotify/images')
    audio = models.FileField(upload_to='spotify/audio')
    created_on = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.song_author

    



