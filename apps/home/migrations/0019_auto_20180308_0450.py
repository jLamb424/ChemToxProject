# Generated by Django 2.0.2 on 2018-03-08 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20180308_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiment_citation_relation',
            name='pmid',
            field=models.IntegerField(null=True),
        ),
    ]