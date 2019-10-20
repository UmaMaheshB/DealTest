from django.db import models
from datetime import datetime
# Create your models here.
class Deal(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField("Image-Url",max_length=500)
    description = models.TextField(max_length=500)
    terms = models.TextField(max_length=500)
    start_date_time = models.DateTimeField(default=datetime.now())
    end_date_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

