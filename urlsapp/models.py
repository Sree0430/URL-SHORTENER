from django.db import models

class ShortURL(models.Model):
    code = models.SlugField(max_length=16, unique=True)
    long_url = models.URLField()
    clicks = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} -> {self.long_url}"
