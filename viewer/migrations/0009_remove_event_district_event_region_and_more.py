# Generated by Django 4.1.1 on 2024-07-05 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0008_remove_event_region_event_district_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='district',
        ),
        migrations.AddField(
            model_name='event',
            name='region',
            field=models.CharField(choices=[('JM', 'Jihomoravský'), ('JC', 'Jihočeský'), ('KA', 'Karlovarský'), ('KR', 'Královéhradecký'), ('LI', 'Liberecký'), ('MO', 'Moravskoslezský'), ('OL', 'Olomoucký'), ('PA', 'Pardubický'), ('PL', 'Plzeňský'), ('PR', 'Praha'), ('ST', 'Středočeský'), ('US', 'Ústecký'), ('VY', 'Vysočina'), ('ZL', 'Zlínský')], default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(20)]),
        ),
    ]