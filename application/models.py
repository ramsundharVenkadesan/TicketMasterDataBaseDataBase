from django.db import models

# Create your models here.
class Event(models.Model):

    id = models.AutoField(primary_key=True)

    event_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    venue = models.CharField(max_length=255)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)

    image = models.URLField()
    event_url = models.URLField()


    def __str__(self) -> str: return f"{self.name} -> {self.city}"