# Generated by Django 4.2.5 on 2023-09-16 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Demande', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demande',
            old_name='Code_cong',
            new_name='congé',
        ),
        migrations.RenameField(
            model_name='demande',
            old_name='CIN',
            new_name='employe',
        ),
        migrations.RenameField(
            model_name='demande',
            old_name='Num_dem',
            new_name='id',
        ),
    ]
