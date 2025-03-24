from django.db import models

# Create your models here.
class Tache(models.Model):
    description = models.CharField(max_length=255)
    dateTache = models.DateField()  

    def __str__(self):
        return f"Tâche {self.idTache}: {self.description} - {self.dateTache}"