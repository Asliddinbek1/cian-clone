# Generated by Django 4.0.4 on 2022-05-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_home_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='image',
            field=models.ImageField(default=True, upload_to='images'),
        ),
    ]
