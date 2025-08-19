from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ListaZadan
from .serializers import ListaZadanSerializer

# Create your views here.

class ListaZadanCreate(APIView):
    def get(self, request):
        zadania = ListaZadan.objects.all()
        for zadanie in zadania:
            zadanie.updateStatusIfExpired()
            zadanie.updateStatusIfCompleted()
        serializer = ListaZadanSerializer(zadania, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ListaZadanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ListaZadanDetail(APIView):
    def getObject(self, pk):
        try:
            return ListaZadan.objects.get(pk=pk)
        except ListaZadan.DoesNotExist:
            return None

    def get(self, request, pk):
        zadanie = self.getObject(pk)
        if not zadanie:
            return Response({"error": "Nie ma"}, status=status.HTTP_404_NOT_FOUND)
        zadanie.updateStatusIfExpired()
        zadanie.updateStatusIfCompleted()
        serializer = ListaZadanSerializer(zadanie)
        return Response(serializer.data)

    def put(self, request, pk):
        zadanie = self.getObject(pk)
        if not zadanie:
            return Response({"error": "Nie ma"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ListaZadanSerializer(zadanie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        zadanie = self.getObject(pk)
        if not zadanie:
            return Response(status=status.HTTP_404_NOT_FOUND)
        zadanie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)