
from django.db import models

# Create your models here.


class Depense(models.Model):
   HABILLEMENT = 'HA'
   MANAGER = 'MA'
   NUTRITION = 'NU'
   TRANSPORT = 'TR'
   OEUVRES_DE_CHARITE  = 'CR'
   INVESTISSEMENT = 'INV'
   CREDITS = 'CR'
   AUTRES = 'O'

   choiCat = [
    ('HA', 'Habillement'),
    ('ME', 'Menager'),
    ('NU', 'Nutrition'),
    ('TR', 'Transport'),
    ('OC', 'Oeuvres de Charité'),
    ('INV', 'Investissement'),
    ('CR', 'Credits'),
    ('O', 'Autres'),
    ]
    
   categorie = models.CharField(max_length=25,choices=choiCat,default=HABILLEMENT)
   description = models.CharField(max_length=25)
   date = models.DateTimeField(auto_now_add=True)
   montant= models.IntegerField(null=True)


   def __str__(self):
        return str(self.categorie) +" "+self.description + " " +str(self.montant) +  " " + str(self.date)
    
class Budget(models.Model):
   budgets = models.BigIntegerField(null=True)
  # def __str__(self):
   #     return Budget.budgets