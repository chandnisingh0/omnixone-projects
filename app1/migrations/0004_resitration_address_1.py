# Generated by Django 3.2.10 on 2022-02-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_remove_resitration_address_1'),
    ]

    operations = [
        migrations.AddField(
            model_name='resitration',
            name='address_1',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
