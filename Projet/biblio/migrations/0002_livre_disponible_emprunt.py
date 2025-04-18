# Generated by Django 5.1.5 on 2025-04-08 21:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblio', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='livre',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Emprunt_at', models.DateTimeField(auto_now_add=True)),
                ('livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprunts', to='biblio.livre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emprunts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
