from django.db import models


class ContactMe(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField()
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.phone


class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    message = models.TextField()

    is_published = models.BooleanField(default=False)

    update_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

