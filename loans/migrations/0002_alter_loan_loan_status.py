# Generated by Django 5.1.2 on 2024-10-30 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='loan_status',
            field=models.CharField(choices=[('Active', 'Ativo'), ('Returned', 'Devolvido')], default='Active', max_length=20),
        ),
    ]
