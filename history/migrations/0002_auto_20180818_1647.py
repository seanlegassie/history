# Generated by Django 2.1 on 2018-08-18 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='histimage',
            name='Year',
            field=models.IntegerField(),
        ),
    ]
