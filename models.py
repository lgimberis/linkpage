from django.db import models

class Link(models.Model):
    link_text = models.CharField()
    link_url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return