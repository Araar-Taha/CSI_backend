from rest_framework import serializers
from models import Tache

class TacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tache
        fields = ['description', 'dateTache']
        
    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance