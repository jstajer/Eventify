# Generated by Django 4.2 on 2024-07-22 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0014_alter_event_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
