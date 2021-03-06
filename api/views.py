from django.shortcuts import render
from .models import Song,Podcast,Audiobook
from .serializers import SongSerializer,PodcastSerializer,AudiobookSerializer
from rest_framework import viewsets

class Songs_File(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class Podcasts_File(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

class Audiobooks_File(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer
