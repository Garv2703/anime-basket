from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Reviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.IntegerField()
    name = models.CharField(max_length=255)
    comment = models.CharField(max_length=1000)
    episode_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)