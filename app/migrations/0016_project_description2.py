# Generated by Django 3.0.5 on 2020-04-27 21:30

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description2',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]