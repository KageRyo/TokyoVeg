# Generated by Django 3.2 on 2024-07-10 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20240710_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='introduction',
            field=models.CharField(max_length=100),
        ),
    ]
