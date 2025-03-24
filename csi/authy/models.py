from django.db import models
from workshop.models import Atelier
from tasks.models import Tache

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    USER_TYPE_CHOICES = [
        ('Participant', 'Participant'),
        ('Woofer', 'Woofer'),
        ('Admin', 'Admin'),
    ]
    #an AbstractUser django class have already the fields that we need
    #we just need to add the user-type attribute
    woofer = models.OneToOneField("Woofer", null=True, blank=True, on_delete=models.CASCADE)
    participant = models.OneToOneField("Participant", null=True, blank=True, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=12, choices=USER_TYPE_CHOICES, default='Participant',)
    #username is already included in REQUIRED_FIELDS so i removed it
    REQUIRED_FIELDS = ['password','user_type']
    def __str__(self):
        return "{self.username} ({self.user_type})"
    

class Participant(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='participant_instance')
    # Add additional fields specific to Participant
    # to add later:atelier FK
    ateliers = models.ManyToManyField(Atelier, related_name='participants', blank=True)

    def __str__(self):
        return self.user.username
    


class Woofer(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='woofer_instance')
    # Add additional fields specific to Woofer
    participant_field = models.CharField(max_length=255)
    dateDeNaissance = models.DateField()
    dateDebutSejour = models.DateField()
    taches = models.ManyToManyField(Tache, related_name='woofers')


    def __str__(self):
        return self.user.username