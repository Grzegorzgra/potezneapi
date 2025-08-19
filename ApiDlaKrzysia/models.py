from django.db import models
from django.utils import timezone

# Create your models here.


class ListaZadan(models.Model):

    STATUS_CHOICES = [
        ('Active', 'active'),
        ('Expired', 'expired'),
        ('Done', 'done')
        ]
    task = models.CharField(max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True,default='')
    isCompleted = models.BooleanField(default=False)
    expirationDate = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Active')

    def updateStatusIfCompleted(self):
        if  self.isCompleted:
            self.status = 'Done'
            self.save()

    def updateStatusIfExpired(self):
        if self.expirationDate and self.expirationDate < timezone.now() and self.status == 'Active':
            self.status = 'Expired'
            self.save()

    def __str__(self):
        return f"{self.added} {self.task} - {self.description[:30]}."