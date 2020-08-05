# Generated by Django 2.0.7 on 2020-08-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
                ('section', models.PositiveSmallIntegerField()),
                ('crn', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
