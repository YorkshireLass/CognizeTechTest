from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

import uuid
import os


def validate_extension(document):
    document = str(document)
    extension = os.path.splitext(document)[1]
    # This could be expanded to include Word and PDF docs in future
    acceptable_extensions = ['.txt']
    if not extension in acceptable_extensions:
        raise ValidationError(u'Error: Unsupported file type uploaded.')


class Document(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/%Y/%m/%d', validators=[validate_extension])
    upload_time = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.title


class Words(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    occurences = models.IntegerField(null=True)

    def __str__(self):
        return self.word


class Phrases(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    word = models.ForeignKey(Words, on_delete=models.CASCADE)
    phrase = models.TextField(null=True)

    def __str__(self):
        return self.phrase
        