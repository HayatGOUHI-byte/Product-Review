# Generated by Django 5.1.5 on 2025-04-11 10:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_immatriculation', models.CharField(max_length=9)),
                ('marque', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=30)),
                ('annee', models.CharField(max_length=5)),
                ('kilometrage', models.IntegerField()),
                ('statut', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statut', to='LocationV.statut')),
            ],
        ),
    ]
