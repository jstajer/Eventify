# Generated by Django 4.2 on 2024-07-16 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0010_alter_event_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
