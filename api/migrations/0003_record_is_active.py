# Generated by Django 4.2 on 2023-04-06 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_insert_operations'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]