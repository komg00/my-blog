# Generated by Django 4.2.13 on 2024-06-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='intruder_image/default_error.png', null=True, upload_to='intruder_image/%Y/%m/%d/'),
        ),
    ]
