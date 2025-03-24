from django.db import models
from authy.models import Woofer
from workshop.models import Produit

# Create your models here.
class Vente(models.Model):
    #We have t add Payement later
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField()
    woofer = models.ForeignKey(Woofer,on_delete=models.CASCADE,related_name="ateliers_produit")
    produits = models.ManyToManyField(Produit,related_name='ventes_produit')
    payement = models.ForeignKey('Payement',null=True,on_delete=models.SET_NULL,related_name="ateliers_produit")
    
    
class Payement(models.Model):
    PAYEMENT_TYPE_CHOICES=[('PE','PE'),
                           ('PC','PC'),]
    date = models.DateTimeField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    payement_type = models.CharField(max_length=7, choices=PAYEMENT_TYPE_CHOICES, default='Espese',)
    nomDebiteur = models.CharField(max_length=20,null=True)
    dateExpiration = models.DateField(null=True)
    vente = models.ForeignKey(Vente,on_delete=models.CASCADE,related_name="vente_payement")
    codeCarte = models.DecimalField(max_digits=16,decimal_places=0)

    