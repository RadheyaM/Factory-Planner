# Generated by Django 3.2.16 on 2022-11-25 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0013_alter_week_start_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pack',
            options={'permissions': [('can_edit_pack', 'Can edit a packing configuration'), ('can_create_pack', 'Can create a packing configuration'), ('can_delete_pack', 'Can delete a packing configuration')]},
        ),
        migrations.AlterModelOptions(
            name='packingrun',
            options={'ordering': ['day'], 'permissions': [('can_edit_packing_run', 'Can edit a packing run'), ('can_create_packing_run', 'Can create a packing run'), ('can_delete_packing_run', 'Can delete a packing run')]},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('can_edit_product', 'Can edit a product'), ('can_create_product', 'Can create a product'), ('can_delete_product', 'Can delete a product')]},
        ),
        migrations.AlterModelOptions(
            name='run',
            options={'permissions': [('can_edit_run', 'Can edit a run'), ('can_create_run', 'Can create a run'), ('can_delete_run', 'Can delete a run')]},
        ),
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ['-start_date'], 'permissions': [('can_edit_week', 'Can edit a week plan'), ('can_create_week', 'Can create a week plan'), ('can_delete_week', 'Can delete a week plan')]},
        ),
    ]
