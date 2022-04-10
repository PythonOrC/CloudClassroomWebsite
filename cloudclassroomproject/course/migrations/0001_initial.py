# Generated by Django 4.0.3 on 2022-04-10 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='course_pics')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('availability', models.BooleanField(default=True)),
                ('url', models.CharField(default='\\course\\', max_length=255)),
                ('difficulty', models.CharField(default='Beginner', max_length=255)),
                ('teacher', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
