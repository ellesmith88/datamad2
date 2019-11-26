# Generated by Django 2.2.6 on 2019-11-26 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmp', '0006_auto_20191126_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('Initial contact', 'Initial contact'), ('DMP comms', 'DMP comms'), ('Progress', 'Progress'), ('Data delivery', 'Data delivery')], max_length=200, null=True),
        ),
    ]
