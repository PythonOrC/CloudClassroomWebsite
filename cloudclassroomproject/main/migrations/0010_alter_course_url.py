# Generated by Django 4.0.3 on 2022-04-08 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_course_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='url',
            field=models.CharField(default='\\course\\', max_length=255),
        ),
    ]
