# Generated by Django 3.0.8 on 2020-07-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0005_post_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pic',
            field=models.ImageField(null=True, upload_to='.images'),
        ),
    ]