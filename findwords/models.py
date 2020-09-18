from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
import uuid
import os


def validate_extension(document):
    document = str(document)
    extension = os.path.splitext(document)[1]
    acceptable_extensions = ['.txt']#, '.doc', '.docx', '.pdf']
    if not extension in acceptable_extensions:
        raise ValidationError(u'Error: Unsupported file type uploaded.')


class Document(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_extension])
    upload_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title
    
    #def create(self):
    #    self.title = os.path.splitext(self.document)[0]
    #    self.save()
        