# Generated by Django 3.2.12 on 2022-09-24 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_remove_controller_testingbydirecthtml'),
    ]

    operations = [
        migrations.AlterField(
            model_name='controller',
            name='insideContains',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
