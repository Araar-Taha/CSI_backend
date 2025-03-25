from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Tache
from .serializers import TacheSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from authy.CustomPermission import IsAdmin

class CreateTacheView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def post(self, request):
        serializer = TacheSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveTacheView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def get(self, request):
        pk = request.data.get('pk')  
        if not pk:
            return Response({"error": "L'ID de la tâche est requis."}, status=status.HTTP_400_BAD_REQUEST)
        
        tache = get_object_or_404(Tache, pk=pk)
        serializer = TacheSerializer(tache)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateTacheView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def put(self, request):
        pk = request.data.get('pk')  
        if not pk:
            return Response({"error": "L'ID de la tâche est requis."}, status=status.HTTP_400_BAD_REQUEST)

        tache = get_object_or_404(Tache, pk=pk)
        serializer = TacheSerializer(tache, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTacheView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]
    def delete(self, request):
        pk = request.data.get('pk')  
        if not pk:
            return Response({"error": "L'ID de la tâche est requis."}, status=status.HTTP_400_BAD_REQUEST)

        tache = get_object_or_404(Tache, pk=pk)
        tache.delete()
        return Response({"message": "Tâche supprimée avec succès"}, status=status.HTTP_204_NO_CONTENT)
