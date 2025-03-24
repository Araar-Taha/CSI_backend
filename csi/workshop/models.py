from django.db import models
# from authy.models import Woofer

# Create your models here.

class Produit(models.Model):
    CATEGORIES_CHOICES = [
        ('Oeufs', 'Oeufs'),
        ('Produit_laitiers', 'Produit_laitiers'),
        ('Legumes', 'Legumes'),
        ('Fruits', 'Fruits'),
    ]
    nom = models.CharField(max_length=20)
    categorie = models.CharField(max_length=17, choices=CATEGORIES_CHOICES)

class Atelier(models.Model):
    theme = models.CharField(max_length=50)
    date = models.DateTimeField()
    woofer = models.ForeignKey('authy.Woofer', on_delete=models.CASCADE, related_name='ateliers')
    produit = models.ForeignKey(Produit,null=True,on_delete=models.SET_NULL,related_name="ateliers_produit") 
    

    def __str__(self):
        return self.title


