# Generated by Django 5.0.7 on 2024-11-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CVGenerator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CVInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('jobTitle', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('requirements', models.TextField()),
                ('experienceYears', models.CharField(choices=[('Menos de un año', 'Menos de un año'), ('1 a 3 años', '1 a 3 años'), ('4 a 6 años', '4 a 6 años'), ('7 a 10 años', '7 a 10 años'), ('Más de 10 años', 'Más de 10 años')], max_length=20)),
            ],
        ),
    ]
