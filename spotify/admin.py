from django.contrib import admin
from . models import SpotMusic 

class SpotMusicAdmin(admin.ModelAdmin):
    list_display = ('user','song_author','song_title','song_image','audio','created_on')
admin.site.register(SpotMusic, SpotMusicAdmin)

# Register your models here.
