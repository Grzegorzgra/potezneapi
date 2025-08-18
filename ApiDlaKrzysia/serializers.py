from rest_framework import serializers
from .models import ListaZadan

class ListaZadanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListaZadan
        fields = ['id', "added", 'task', 'description']