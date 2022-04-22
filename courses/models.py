from django.db import models


# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=1000, null=True)
    desc = models.TextField(blank=True, max_length=100, null=True)
    trainer = models.CharField(max_length=100, null=True)

    # published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
