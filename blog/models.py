from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    publish_date = models.DateField()

    def __str__(self):
        return self.title