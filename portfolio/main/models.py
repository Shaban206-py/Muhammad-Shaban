# models.py

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='main/images/')  # Ensure MEDIA settings are configured
    repo_url = models.URLField()

    def __str__(self):
        return self.name
