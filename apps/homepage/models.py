from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    email = models.EmailField()
    skype = models.CharField(max_length=50)
    jabber = models.CharField(max_length=50)
    bdate = models.DateField()
    bio = models.CharField(max_length=500)
    contacts = models.CharField(max_length=500)

    def __str__(self):
        return self.name
