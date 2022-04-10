# Generated by Django 4.0.3 on 2022-04-10 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_difficulty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], default='Beginner'),
        ),
    ]