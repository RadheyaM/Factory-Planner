# Generated by Django 3.2.16 on 2022-11-03 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0003_alter_packing_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='complete',
            field=models.CharField(choices=[('No', 'No'), ('Yes', 'Yes')], max_length=5),
        ),
    ]
