# Generated by Django 4.2 on 2024-07-20 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0013_alter_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='region',
            field=models.CharField(choices=[('JC', 'Jihočeský'), ('JM', 'Jihomoravský'), ('KA', 'Karlovarský'), ('KR', 'Královéhradecký'), ('LI', 'Liberecký'), ('MO', 'Moravskoslezský'), ('OL', 'Olomoucký'), ('PA', 'Pardubický'), ('PL', 'Plzeňský'), ('PR', 'Praha'), ('ST', 'Středočeský'), ('US', 'Ústecký'), ('VY', 'Vysočina'), ('ZL', 'Zlínský')], default='', max_length=40),
        ),
    ]
