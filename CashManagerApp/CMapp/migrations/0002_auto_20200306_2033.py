# Generated by Django 3.0.4 on 2020-03-06 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateur',
            old_name='Budget',
            new_name='budget',
        ),
    ]
