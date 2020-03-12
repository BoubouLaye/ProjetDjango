# Generated by Django 3.0.4 on 2020-03-11 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CMapp', '0002_auto_20200310_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depense',
            name='categorie',
            field=models.CharField(choices=[('HA', 'Habillement'), ('ME', 'Menager'), ('NU', 'Nutrition'), ('TR', 'Transport'), ('OC', 'Oeuvres de Charité'), ('INV', 'Investissement'), ('CR', 'Credits'), ('O', 'Autres')], default='HA', max_length=25),
        ),
        migrations.AlterField(
            model_name='depense',
            name='description',
            field=models.CharField(max_length=25),
        ),
    ]
