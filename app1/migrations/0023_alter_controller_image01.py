# Generated by Django 3.2.12 on 2022-09-26 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_auto_20220926_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='image01',
            field=models.ImageField(null=True, upload_to='controller1OriImage'),
        ),
    ]
