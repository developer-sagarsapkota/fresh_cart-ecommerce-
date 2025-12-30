from rest_framework import serializers
# whatever user model we have set for the auth user model we should use for registration
from django.contrib.auth import get_user_model

User = get_user_model()

# using model serializer to store the data 
class UserRegisterSerializer(serializers.ModelSerializer):
    # once the user is created it should be write only. the password should not go in response
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["id", "email", "username", "password"]
    
    # to validate and hash the password as well as return the user
    def create(self, validated_data):
        # whatever the data comes it will use and create the data
        # **validated data means take data and store 
        user = User.objects.create_user(**validated_data)
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "first_name", "last_name"]
        read_only_fields = ["id", "email"]
