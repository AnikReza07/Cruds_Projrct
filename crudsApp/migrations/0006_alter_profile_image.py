# Generated by Django 4.2.5 on 2023-09-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudsApp', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='def.png', upload_to='prof_pic/'),
        ),
    ]
