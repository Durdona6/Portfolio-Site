from django.db import models

class About(models.Model):
    fullname = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(upload_to='about/')
    description = models.TextField()
    twitter = models.CharField(max_length=200)
    facebook = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)

    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

class Section(models.Model):
    title = models.CharField(max_length=200)
    number = models.IntegerField()

    def __str__(self) -> str:
        return self.title
