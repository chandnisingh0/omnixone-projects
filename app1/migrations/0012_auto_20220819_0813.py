# Generated by Django 3.2.10 on 2022-08-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_auto_20220815_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='blurController',
            field=models.ImageField(default='blur.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='embeddedlinux',
            name='blurEmbeddedLinux',
            field=models.ImageField(default='blur.jpg', null=True, upload_to=''),
        ),
    ]
