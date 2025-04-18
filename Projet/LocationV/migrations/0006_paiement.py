# Generated by Django 5.1.5 on 2025-04-11 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocationV', '0005_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.IntegerField()),
                ('mode_paiement', models.CharField(max_length=23)),
                ('date_paiement', models.DateTimeField()),
                ('etat_paiement', models.CharField(max_length=100)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='LocationV.reservation')),
            ],
        ),
    ]
