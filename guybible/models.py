from django.db import models

class Podcast(models.Model):
    audio_file = models.FileField(
        upload_to='audio/', null=True, blank=True)
    title = models.CharField(
        max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
