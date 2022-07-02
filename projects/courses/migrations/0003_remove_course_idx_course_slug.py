# Generated by Django 4.0.5 on 2022-07-02 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_options_course_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='idx',
        ),
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]