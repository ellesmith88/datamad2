# Generated by Django 2.2.6 on 2019-11-21 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0009_auto_20191121_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importedgrant',
            name='call',
        ),
    ]