import uuid
from django.db import models

class Person(models.Model):

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

    def model_to_dict(self):
        removed_keys = ['_state']
        new = {}
        for key in self.__dict__:
            if key not in removed_keys:
                new[key] = str(self.__dict__[key])
        return new
