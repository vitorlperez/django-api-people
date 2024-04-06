import uuid
from django.db import models

class Person(models.Model):
    db_table = '"person"'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    cpf = models.CharField(max_length=14)
    sex = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    height = models.FloatField()
    weight = models.FloatField()
