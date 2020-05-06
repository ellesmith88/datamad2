# Generated by Django 2.2.10 on 2020-04-27 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0003_auto_20200403_0803'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('jira_project', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='grant',
            name='assigned_data_centre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_data_centre', to='datamad2.DataCentre'),
        ),
        migrations.AlterField(
            model_name='grant',
            name='other_data_centre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='other_data_centre', to='datamad2.DataCentre'),
        ),
        migrations.AlterField(
            model_name='user',
            name='data_centre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='datamad2.DataCentre'),
        ),
    ]