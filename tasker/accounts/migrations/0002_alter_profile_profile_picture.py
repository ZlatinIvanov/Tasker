# Generated by Django 5.0.3 on 2024-04-07 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.FileField(blank=True, default=None, null=True, upload_to='profile_pictures'),
        ),
    ]
