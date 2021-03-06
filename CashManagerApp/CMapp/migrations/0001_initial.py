# Generated by Django 3.0.4 on 2020-03-10 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budgets', models.BigIntegerField(unique_for_month='date')),
            ],
        ),
        migrations.CreateModel(
            name='Depense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(choices=[('HA', 'Habillement'), ('ME', 'Menager'), ('NU', 'Nutrition'), ('TR', 'Transport'), ('OC', 'Oeuvres de Charité'), ('INV', 'Investissement'), ('CR', 'Credits'), ('O', 'Autres')], default='FR', max_length=25)),
                ('description', models.TextField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('montant', models.IntegerField(null=True)),
                ('bud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CMapp.Budget')),
            ],
        ),
    ]
