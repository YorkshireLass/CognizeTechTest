# Generated by Django 2.2.16 on 2020-09-17 17:38

from django.db import migrations, models
import findwords.models


class Migration(migrations.Migration):

    dependencies = [
        ('findwords', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(editable=False, upload_to='documents/', validators=[findwords.models.validate_extension]),
        ),
    ]