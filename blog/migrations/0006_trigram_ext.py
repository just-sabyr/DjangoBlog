# Generated by Django 5.1 on 2024-09-17 05:16

from django.db import migrations
from django.contrib.postgres.operations import TrigramExtension

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_trigram_ext'),
    ]

    operations = [
        TrigramExtension()
    ]
