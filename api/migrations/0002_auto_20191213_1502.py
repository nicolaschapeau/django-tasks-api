# Generated by Django 3.0 on 2019-12-13 15:02

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name_plural': 'User Profile'},
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Task title')),
                ('description', models.TextField(max_length=500, verbose_name='Task description')),
                ('completed', models.BooleanField(default=False, verbose_name='Task status')),
                ('task_picture', models.ImageField(upload_to=api.models.task_directory_path, verbose_name='Task picture')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]