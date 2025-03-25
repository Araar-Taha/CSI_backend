from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from authy.models import Woofer
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
    permission_classes = [IsAuthenticated]
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
    
class AffectTacheToWooferView(APIView):
    permission_classes = [IsAuthenticated,IsAdmin]

    def post(self, request, *args, **kwargs):
        
        woofer_username = request.data.get('woofer_username')
        tache_id = request.data.get('tache_id')

        if not woofer_username or not tache_id:
            return Response({"error": "Les champs 'woofer_username' et 'tache_id' sont obligatoires."}, status=status.HTTP_400_BAD_REQUEST)

        
        woofer = get_object_or_404(Woofer, user__username=woofer_username)
        
        
        tache = get_object_or_404(Tache, pk=tache_id)

        # Vérifier si la date de la tâche est entre la date de début et la date de fin du séjour du Woofer
        if not (woofer.dateDebutSejour <= tache.dateTache <= woofer.dateFinSejour):
            raise ValidationError("La date de la tâche doit être entre la date de début et la date de fin du séjour du Woofer.")

        
        woofer.taches.add(tache)

       
        return Response({"message": f"Tâche {tache.id} affectée au Woofer {woofer_username}."}, status=status.HTTP_200_OK)    
