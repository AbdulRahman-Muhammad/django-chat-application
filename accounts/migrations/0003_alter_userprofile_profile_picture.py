# Generated by Django 4.1 on 2022-09-05 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='images/profile/profile-circled (1).svg', upload_to='images/profile/'),
        ),
    ]
