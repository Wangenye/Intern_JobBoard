# Generated by Django 3.1.6 on 2021-03-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfileApp', '0008_auto_20210324_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='companydetail',
            name='company_ceo',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
