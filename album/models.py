from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from seller1.models import SellBusiness



class File(models.Model):
    file_id = models.AutoField(primary_key=True, auto_created=True)
    file = models.FileField(upload_to='files/')
    name = models.CharField(max_length=200, blank=True, default=True)
    # seller = models.ManyToManyField(SellBusiness, blank=True, null=True)

    def __str__(self):
        return self.file.name

    def save(self, *args, **kwargs):
        self.name = self.file.name
        super(File, self).save(*args, **kwargs)


class KAlbumForFile(models.Model):
    album_id = models.UUIDField(primary_key=True)
    files = models.ManyToManyField(File, blank=True, null=True)
    seller = models.ManyToManyField(SellBusiness, blank=True, null=True)

@receiver(post_delete, sender=File)
def submission_delete(sender, instance, **kwargs):
    instance.file.delete(False) 


