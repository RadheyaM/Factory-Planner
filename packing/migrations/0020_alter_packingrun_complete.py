# Generated by Django 3.2.16 on 2022-12-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0019_packingrun_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packingrun',
            name='complete',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], default='No', max_length=50),
        ),
    ]