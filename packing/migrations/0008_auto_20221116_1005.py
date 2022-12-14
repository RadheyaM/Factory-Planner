# Generated by Django 3.2.16 on 2022-11-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packing', '0007_alter_packing_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='packing',
            options={'ordering': ['day']},
        ),
        migrations.AlterModelOptions(
            name='week',
            options={'ordering': ['-start_date']},
        ),
    ]
