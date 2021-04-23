from django.db import models

class upload_old(models.Model):
    old_name = models.CharField(max_length=200)
    old_Image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.old_name


class upload_new(models.Model):
    new_name = models.CharField(max_length=200)
    new_Image = models.ImageField(upload_to='media')
    def __str__(self):
        return self.new_name