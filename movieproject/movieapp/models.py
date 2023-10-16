from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=250)
    desc=models.CharField(max_length=1000)
    year=models.IntegerField()
    img=models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
