# Generated by Django 5.1.1 on 2024-10-18 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='status',
            field=models.CharField(default='pending', max_length=255),
        ),
    ]
