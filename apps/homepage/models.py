from django.db import models


class Human(models.Model):
    Name = models.CharField(max_length=50)
    sName = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Skype = models.CharField(max_length=50)
    Jabber = models.CharField(max_length=50)
    bDate = models.DateField()
    Bio = models.CharField(max_length=500)
    Contacts = models.CharField(max_length=500)

    def __str__(self):
        return self.Name
