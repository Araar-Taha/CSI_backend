from rest_framework import serializers
from .models import Utilisateur,Woofer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'username','first_name','last_name', 'email', 'user_type', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class WooferSerializer(serializers.ModelSerializer):
      class Meta:
        model = Woofer 
        fields ='__all__'
          