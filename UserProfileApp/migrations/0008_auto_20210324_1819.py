# Generated by Django 3.1.6 on 2021-03-24 18:19

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('UserProfileApp', '0007_auto_20210324_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('company_about', models.TextField(max_length=500, null=True)),
                ('company_logo', models.ImageField(upload_to='Employer/company_logos/')),
                ('company_email', models.EmailField(blank=True, max_length=254)),
                ('company_tel', models.CharField(blank=True, max_length=20)),
                ('company_country', django_countries.fields.CountryField(max_length=2)),
                ('company_city', models.CharField(blank=True, max_length=30)),
                ('company_website', models.URLField(blank=True)),
                ('company_location', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='userdetail',
            name='jobseeker_image',
            field=models.ImageField(blank=True, upload_to='Jobseeker/Images/'),
        ),
    ]
