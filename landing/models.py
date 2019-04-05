from django.db import models

class Subscribers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=10)

    def __str__(self):
        return "%s %s" % (self.name, self.email)
