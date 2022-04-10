# Generated by Django 4.0.3 on 2022-04-10 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('main', '0011_course_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cart',
            field=models.ManyToManyField(blank=True, related_name='cart', to='course.course'),
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='courses',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='courses',
            field=models.ManyToManyField(blank=True, to='course.course'),
        ),
        migrations.DeleteModel(
            name='Course',
        ),
    ]