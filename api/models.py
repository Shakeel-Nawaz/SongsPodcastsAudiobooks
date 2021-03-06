from django.db import models
from datetime import datetime,timedelta
from django.core.exceptions import ValidationError
import django.utils.timezone

#--------------------Creating Song Model--------------------#

def nopastdate(dateu):
    if (dateu + timedelta(minutes=10)) < datetime.now():
        raise ValidationError("Date & Time cannot be in the past & Leave Empty for current date and time ")
    return dateu

class Song(models.Model):
    Song_Name = models.CharField(max_length=100)
    Song_Duration = models.PositiveIntegerField()
    Song_Uploaded_Time = models.DateTimeField(
        default=django.utils.timezone.now,
        help_text='Leave Empty for current date and time',
        validators=[nopastdate])

#--------------------Creating Podcast Model--------------------#

def maxentries(entries):
    if len(entries.split(',')) > 10:
        raise ValidationError('Max 10 entries of 100 characters each can be made seperatted by comma')
    return entries
class Podcast(models.Model):
    Podcast_Name = models.CharField(max_length=100)
    Podcast_Duration = models.PositiveIntegerField()
    Podcast_Uploaded_Time = models.DateTimeField(
        default= django.utils.timezone.now,
        validators=[nopastdate])
    Host = models.CharField(max_length=100)
    Participants = models.CharField(
        max_length=1030,
        help_text='Max 10 entries can be made',
        validators=[maxentries])

#--------------------Creating Audiobook Model--------------------#

class Audiobook(models.Model):
    Audiobook_Title = models.CharField(max_length=100)
    Audiobook_Title_Author = models.CharField(max_length=100,)
    Narrator = models.CharField(max_length=100)
    Audiobook_Duration = models.PositiveIntegerField()
    Audiobook_Uploaded_Time = models.DateTimeField(
        default=django.utils.timezone.now,
        validators=[nopastdate])
