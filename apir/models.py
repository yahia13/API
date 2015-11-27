from django.db import models
from django.utils import timezone
from time import time
#function for uploaded files path
def get_upload_file_name(instance, filename):
    return "static/apir/%s_%s" % (str(time()).replace('.','_'), filename)
#the models were to be used for adding data (not working)
class Data(models.Model):

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    created_date = models.DateTimeField(
            default=timezone.now)


