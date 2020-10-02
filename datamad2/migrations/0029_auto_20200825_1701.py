# Generated by Django 2.2.6 on 2020-08-25 16:01

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0028_auto_20200805_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='grant',
            name='dmp_agreed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='grant',
            name='dmp_agreed_date',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='dmp_agreed', when={True}),
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.CharField(blank=True, help_text='Comma separated list of tags to be displayed with the file',
                                   max_length=100),
        ),
    ]