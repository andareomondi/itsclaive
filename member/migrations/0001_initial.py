# Generated by Django 5.1.1 on 2024-10-17 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('venue', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('phone_number', models.IntegerField()),
                ('service_type', models.CharField(max_length=255)),
            ],
        ),
    ]
