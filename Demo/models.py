from django.core.files.storage import FileSystemStorage
from django.db import models
from django.core.files import File

fs = FileSystemStorage(location='/media/photos')

class images(models.Model):

    Title = models.CharField(max_length=10)
    content_image = models.ImageField(upload_to='fs', null=True, blank=True)
    style_image = models.ImageField(upload_to='fs', null=True, blank=True)
    output_image = models.ImageField(upload_to='fs', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.Title)
