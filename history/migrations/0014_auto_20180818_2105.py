# Generated by Django 2.1 on 2018-08-19 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0013_auto_20180818_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histimage',
            name='Photograph',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]
