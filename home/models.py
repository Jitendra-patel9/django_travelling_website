from django.db import models

#makemigrations-> create changes and store in a file
#migrate -> apply the pending changes created by makemigrations

#if you change any this here you are change in database structure so you need to run both above command

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()

    def _str_(self):
        return self.name