# Generated by Django 4.2 on 2024-07-21 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0014_alter_event_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('food', 'Food'), ('music', 'Music'), ('sport', 'Sport'), ('culture', 'Culture'), ('wellness', 'Wellness'), ('experiences', 'Experiences'), ('nature', 'Nature'), ('free', 'Free')], max_length=50),
        ),
    ]
