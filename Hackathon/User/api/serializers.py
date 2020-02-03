from rest_framework import serializers
from User.models import user

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=user
        fields=['username','email','password','Is_University','Is_Candidate','Is_Organization']

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=200)
    password=serializers.CharField(max_length=20)
    class Meta:
        fields=['username','password']
                