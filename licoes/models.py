from django.db import models

class Licao(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo_html = models.TextField()

    def __str__(self):
        return self.titulo
