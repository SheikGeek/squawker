from django.db import models

class Message(models.Model):
    message = models.CharField(max_length=140)
    user = models.ForeignKey('auth.User')
