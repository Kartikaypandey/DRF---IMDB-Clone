from django.db import models

# Create your models here.


class Tweet(models.Model):
    name = models.CharField(max_length=50)
    tweet = models.CharField(max_length=140)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
