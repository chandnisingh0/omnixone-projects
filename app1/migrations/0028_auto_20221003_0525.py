# Generated by Django 3.2.10 on 2022-10-03 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0027_auto_20221002_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='embeddedlinux',
            name='multiImgEmb1',
            field=models.ImageField(null=True, upload_to='original_image'),
        ),
        migrations.AddField(
            model_name='embeddedlinux',
            name='multiImgEmb2',
            field=models.ImageField(null=True, upload_to='original_image'),
        ),
        migrations.AddField(
            model_name='embeddedlinux',
            name='multiImgEmb3',
            field=models.ImageField(null=True, upload_to='original_image'),
        ),
        migrations.AddField(
            model_name='embeddedlinux',
            name='multiImgEmb4',
            field=models.ImageField(null=True, upload_to='original_image'),
        ),
    ]
