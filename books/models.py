from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    url = models.CharField(max_length=256, null=True, blank=True)
    thoughts = models.TextField()
    cover = models.ImageField()
    finished = models.DateTimeField('date finished')

    def __str__(self):
        return self.title
