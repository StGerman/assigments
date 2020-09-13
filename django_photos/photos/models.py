from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="photo", null=True
    )
    image = models.ImageField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comment", null=True
    )
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.text
