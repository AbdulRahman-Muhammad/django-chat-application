# Generated by Django 4.1 on 2022-09-05 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/profile/defaultprofile.png', upload_to='images/profile/'),
        ),
    ]