# Generated by Django 3.1.6 on 2021-03-24 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfileApp', '0005_auto_20210324_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='phone2',
        ),
    ]