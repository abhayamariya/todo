# Generated by Django 4.2.6 on 2023-11-23 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]