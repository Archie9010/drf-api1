# Generated by Django 3.2.16 on 2022-12-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_qdjgyp', upload_to='images/'),
        ),
    ]
