# Generated by Django 3.2.16 on 2022-11-16 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0010_rename_teams_team'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Packaging',
            new_name='Pack',
        ),
        migrations.RenameModel(
            old_name='Packing',
            new_name='PackingRun',
        ),
    ]