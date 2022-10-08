from tabnanny import verbose
from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    nbre = models.FloatField()
    
    class Meta:
        verbose_name=('Personne')
        verbose_name_plural = ('Personnes')
        
    def __str__(self):
        return self.nom
    

# Create your models here.
