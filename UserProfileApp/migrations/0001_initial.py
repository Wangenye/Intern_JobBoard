# Generated by Django 3.1.6 on 2021-04-06 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobsApp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_employer', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('jobseeker_image', models.ImageField(blank=True, upload_to='Jobseeker/Images/')),
                ('last_name', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255, null=True)),
                ('phone', models.CharField(max_length=14, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2)),
                ('role', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='userprofiledetails', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ConversationMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversationmessage', to='jobsApp.application')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conversationmessage', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('company_ceo', models.CharField(blank=True, max_length=20, null=True)),
                ('company_about', models.TextField(blank=True, max_length=500, null=True)),
                ('company_logo', models.ImageField(upload_to='Employer/company_logos/')),
                ('company_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('company_tel', models.CharField(blank=True, max_length=20, null=True)),
                ('company_country', django_countries.fields.CountryField(max_length=2, null=True)),
                ('company_city', models.CharField(blank=True, max_length=30, null=True)),
                ('company_website', models.URLField(blank=True, null=True)),
                ('company_location', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='employerprofile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
