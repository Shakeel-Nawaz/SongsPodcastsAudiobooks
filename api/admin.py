from django.contrib import admin
from .models import Song,Podcast,Audiobook

@admin.register(Song)
class SongAdminPanel(admin.ModelAdmin):
    list_display = ['id','Song_Name','Song_Duration','Song_Uploaded_Time']

@admin.register(Podcast)
class PodcastAdminPanel(admin.ModelAdmin):
    list_display = ['id','Podcast_Name','Podcast_Duration','Podcast_Uploaded_Time','Host','Participants']

@admin.register(Audiobook)
class AudiobookAdminPanel(admin.ModelAdmin):
    list_display = ['id','Audiobook_Title','Audiobook_Title_Author','Narrator','Audiobook_Duration','Audiobook_Uploaded_Time']
