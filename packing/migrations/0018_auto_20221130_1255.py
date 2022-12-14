# Generated by Django 3.2.16 on 2022-11-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0017_auto_20221128_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pack',
            name='srp',
            field=models.CharField(default='No SRP', help_text='Shelf Ready Pack.', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='pack_sz',
            field=models.IntegerField(help_text='Portions Per Pack.'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ppc',
            field=models.FloatField(help_text='Portions Per Case'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ppt',
            field=models.FloatField(help_text='Portions Per Tray.'),
        ),
        migrations.AlterField(
            model_name='run',
            name='name',
            field=models.CharField(help_text="Customer, Name & cases e.g. 'Charducks Trillionaire 230'", max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='week',
            name='status',
            field=models.IntegerField(choices=[(0, 'Planning'), (1, 'Current'), (2, 'Complete')]),
        ),
    ]
