# Generated by Django 2.2.6 on 2020-09-23 10:26

from django.db import migrations, models
import django.db.models.deletion


def migrate_issue_type_data(apps, schema_editor):

    JIRAIssueType = apps.get_model('datamad2','JIRAIssueType')
    Datacentre = apps.get_model('datamad2','Datacentre')

    for datacentre in Datacentre.objects.all():
        datacentre_jira_issue = JIRAIssueType()
        datacentre_jira_issue.datacentre = datacentre
        datacentre_jira_issue.issuetype = datacentre.issuetype
        datacentre_jira_issue.start_date_field = datacentre.start_date_field
        datacentre_jira_issue.end_date_field = datacentre.end_date_field
        datacentre_jira_issue.grant_ref_field = datacentre.grant_ref_field
        datacentre_jira_issue.pi_field = datacentre.pi_field
        datacentre_jira_issue.research_org_field = datacentre.research_org_field
        datacentre_jira_issue.primary_datacentre_field = datacentre.primary_datacentre_field
        datacentre_jira_issue.save()


def migrate_issue_type_data_reverse(apps, schema_editor):

    Datacentre = apps.get_model('datamad2','Datacentre')

    for datacentre in Datacentre.objects.all():
        datacentre_jira_issue = datacentre.jiraissuetype_set.first()

        if datacentre_jira_issue:
            datacentre.issuetype = datacentre_jira_issue.issuetype
            datacentre.start_date_field = datacentre_jira_issue.start_date_field
            datacentre.end_date_field = datacentre_jira_issue.end_date_field
            datacentre.grant_ref_field = datacentre_jira_issue.grant_ref_field
            datacentre.pi_field = datacentre_jira_issue.pi_field
            datacentre.research_org_field = datacentre_jira_issue.research_org_field
            datacentre.primary_datacentre_field = datacentre_jira_issue.primary_datacentre_field
            datacentre.save()


class Migration(migrations.Migration):

    dependencies = [
        ('datamad2', '0031_auto_20200917_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='JIRAIssueType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issuetype', models.IntegerField(blank=True, help_text='JIRA Data Management issue type ID. e.g. 10602', null=True)),
                ('start_date_field', models.CharField(blank=True, help_text='Format: customfield_{{number}}', max_length=100, verbose_name='Start Date Field ID')),
                ('end_date_field', models.CharField(blank=True, help_text='Format: customfield_<number>', max_length=100, verbose_name='End Date Field ID')),
                ('grant_ref_field', models.CharField(blank=True, help_text='Format: customfield_<number>', max_length=100, verbose_name='Grant Ref Field ID')),
                ('pi_field', models.CharField(blank=True, help_text='Format: customfield_<number>', max_length=100, verbose_name='Principle Investigator Field ID')),
                ('research_org_field', models.CharField(blank=True, help_text='Format: customfield_<number>', max_length=100, verbose_name='Research Org Field ID')),
                ('primary_datacentre_field', models.CharField(blank=True, help_text='Format: customfield_<number>', max_length=100, verbose_name='Primary Datacentre Field ID')),
                ('datacentre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datamad2.DataCentre')),
            ],
        ),
        migrations.RunPython(migrate_issue_type_data, migrate_issue_type_data_reverse),
        migrations.RemoveField(
            model_name='datacentre',
            name='end_date_field',
        ),
        migrations.RemoveField(
            model_name='datacentre',
            name='grant_ref_field',
        ),
        migrations.RemoveField(
            model_name='datacentre',
            name='issuetype',
        ),
        migrations.RemoveField(
            model_name='datacentre',
            name='pi_field',
        ),
        migrations.RemoveField(
            model_name='datacentre',
            name='primary_datacentre_field',
        ),
        migrations.RemoveField(
            model_name='datacentre',
            name='research_org_field',
        ),
        migrations.RemoveField(
            model_name='datacentre',
            name='start_date_field',
        ),
    ]
