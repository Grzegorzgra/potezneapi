from django.db import models

# Create your models here.


class ListaZadan(models.Model):
    task = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.added} {self.task} - {self.description[:30]}."