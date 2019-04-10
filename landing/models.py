from django.db import models

class Subscribers(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=10)
    image = models.FileField(upload_to='csv')

    def __str__(self):
        return "%s %s %s" % (self.email, self.name, self.image)
