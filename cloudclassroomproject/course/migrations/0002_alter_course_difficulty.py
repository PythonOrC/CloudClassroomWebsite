# Generated by Django 4.0.3 on 2022-04-10 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='difficulty',
            field=models.CharField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], default='Beginner', max_length=255),
        ),
    ]