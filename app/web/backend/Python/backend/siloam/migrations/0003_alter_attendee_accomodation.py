# Generated by Django 4.1.7 on 2023-03-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siloam', '0002_rename_loaction_attendee_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendee',
            name='accomodation',
            field=models.BooleanField(default=False),
        ),
    ]
