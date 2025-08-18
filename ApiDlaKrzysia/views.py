from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ListaZadan
from .serializers import ListaZadanSerializer

# Create your views here.

class ListaZadanCreate(APIView):
        def get(self, request):
            ListaGet = ListaZadan.objects.all()
            serializer = ListaZadanSerializer(ListaGet, many=True)
            return Response(serializer.data)

        def post(self, request):
            serializer = ListaZadanSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListaZadanDelete(APIView):
    def delete(self, request, pk):
        try:
            ListaDelete = ListaZadan.objects.get(pk=pk)
        except ListaZadan.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        ListaDelete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)