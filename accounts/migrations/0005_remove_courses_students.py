# Generated by Django 2.0.7 on 2020-08-02 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='students',
        ),
    ]
