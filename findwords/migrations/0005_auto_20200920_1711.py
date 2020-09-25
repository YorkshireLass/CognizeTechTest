# Generated by Django 2.2.16 on 2020-09-20 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findwords', '0004_auto_20200920_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='phrases',
            name='occurences',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='phrases',
            name='phrase',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='words',
            name='occurences',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='words',
            name='word',
            field=models.CharField(max_length=50),
        ),
    ]
