# Generated by Django 3.2.16 on 2022-12-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0025_remove_week_unique_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='week',
            name='status',
            field=models.IntegerField(choices=[(0, 'Planning'), (1, 'Current'), (2, 'Complete'), (3, 'Delete')]),
        ),
    ]
