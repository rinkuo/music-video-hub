from django.db import models
import os
import random
import string

def custom_upload_to(instance, filename):
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return os.path.join('covers/', f'{random_string}_{filename}')

class Track(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=255, blank=True)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to=custom_upload_to, blank=True, null=True, max_length=500)
    audio_file = models.FileField(upload_to='tracks/', blank=False, max_length=500)

    def __str__(self):
        return self.title
