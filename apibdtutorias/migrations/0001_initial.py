# Generated by Django 4.1.6 on 2023-02-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfc', models.CharField(max_length=13)),
                ('periodo', models.CharField(max_length=50)),
                ('carrera', models.CharField(max_length=50)),
            ],
        ),
    ]
