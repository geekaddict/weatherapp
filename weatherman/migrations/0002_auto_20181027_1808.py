# Generated by Django 2.0.6 on 2018-10-27 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherman', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name_plural': 'cities'},
        ),
    ]