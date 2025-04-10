# Generated by Django 5.1.5 on 2025-04-10 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormUP', '0003_formation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formation',
            name='cours',
        ),
        migrations.RemoveField(
            model_name='formation',
            name='formateur',
        ),
        migrations.AddField(
            model_name='formation',
            name='cours',
            field=models.ManyToManyField(related_name='formations', to='FormUP.cours'),
        ),
        migrations.AddField(
            model_name='formation',
            name='formateur',
            field=models.ManyToManyField(related_name='formations_donnee', to='FormUP.formateur'),
        ),
    ]
