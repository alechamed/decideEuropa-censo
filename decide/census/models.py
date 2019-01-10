from django.db import models
from jsonschema._validators import maxLength


class Census(models.Model):
    voting_id = models.PositiveIntegerField()
    voter_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (('voting_id', 'voter_id'),)

class Usuario(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50) #Único
    username = models.CharField(max_length = 50) #Único
    password = models.CharField(max_length = 50)
    is_staff = models.BooleanField(null=false) #True or false
    is_active = models.BooleanField(null=false) #Activo o inactivo 
    date_joined = models.DateField(null=false)