from django.db import models

class AppOs(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField(max_length=70, blank=True, null=True, unique=True, default=None)
    data = models.DateField()

    def __str__(self):
        return self.nome