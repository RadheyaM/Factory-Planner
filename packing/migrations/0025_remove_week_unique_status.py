# Generated by Django 3.2.16 on 2022-12-07 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0024_week_unique_status'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='week',
            name='unique_status',
        ),
    ]
