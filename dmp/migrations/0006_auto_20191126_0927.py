# Generated by Django 2.2.6 on 2019-11-26 09:27

from django.db import migrations, models
import django.db.models.deletion
import sizefield.models


class Migration(migrations.Migration):

    dependencies = [
        ('dmp', '0005_dataproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataproduct',
            name='contact1',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact 1'),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='contact2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Contact 2'),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='datavol',
            field=sizefield.models.FileSizeField(default=0, verbose_name='Data Volume'),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='deliverydate',
            field=models.DateField(blank=True, null=True, verbose_name='Delivery Date'),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='dataproduct',
            name='sciSupContact',
            field=models.ForeignKey(blank=True, help_text='Data centre contact for this data', null=True, on_delete=django.db.models.deletion.PROTECT, to='dmp.Person'),
        ),
        migrations.AlterField(
            model_name='project',
            name='PIemail',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='PI email'),
        ),
        migrations.AlterField(
            model_name='project',
            name='dmp_agreed',
            field=models.DateField(blank=True, help_text='Date format dd/mm/yyyy', null=True, verbose_name='DMP Agreed on'),
        ),
        migrations.AlterField(
            model_name='project',
            name='initial_contact',
            field=models.DateField(blank=True, help_text='Date format dd/mm/yyyy', null=True, verbose_name='Initial Contact on'),
        ),
        migrations.AlterField(
            model_name='project',
            name='other_dataCentres',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Other Data Centres'),
        ),
        migrations.AlterField(
            model_name='project',
            name='primary_dataCentre',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Primary Data Centre'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('Initial Contact', 'Initial contact'), ('DMP Comms', 'DMP comms'), ('Progress', 'Progress'), ('Data Delivery', 'Data delivery')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='sciSupContact',
            field=models.ForeignKey(blank=True, help_text='Data centre contact for this project', null=True, on_delete=django.db.models.deletion.PROTECT, to='dmp.Person'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sciSupContact2',
            field=models.ForeignKey(blank=True, help_text='Data centre contact for this project', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sciSupContact2s', to='dmp.Person'),
        ),
    ]
