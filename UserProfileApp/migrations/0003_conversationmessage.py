# Generated by Django 3.1.6 on 2021-02-05 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobsApp', '0002_application'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UserProfileApp', '0002_auto_20210204_2037'),
    ]

    operations = [
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
    ]
