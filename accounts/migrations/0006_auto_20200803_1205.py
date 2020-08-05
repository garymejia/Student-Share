# Generated by Django 2.0.7 on 2020-08-03 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_courses_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Courses')),
            ],
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='courses',
        ),
        migrations.AddField(
            model_name='attends',
            name='userProfile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.UserProfile'),
        ),
        migrations.AddField(
            model_name='courses',
            name='userProfiles',
            field=models.ManyToManyField(through='accounts.Attends', to='accounts.UserProfile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='classes',
            field=models.ManyToManyField(through='accounts.Attends', to='accounts.Courses'),
        ),
    ]