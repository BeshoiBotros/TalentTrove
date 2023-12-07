
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def usernameAlreadyExist(username):
    return User.objects.filter(username=username).exists()
def emailAlreadyExist(email):
    return User.objects.filter(email=email).exists()

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    
    def validate(self, attrs):

        username = attrs.get('username')
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        email = attrs.get('email')

        if password != confirm_password:
            raise serializers.ValidationError({'passwords' : 'password does not matching with password confermation'})
        if password == None:
            raise serializers.ValidationError({'password' : 'password must be set'})
        if username == None:
            raise serializers.ValidationError({'username' : 'username must be set'})
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(f'{e}')
        if usernameAlreadyExist(username):
            raise serializers.ValidationError({'username' : 'username already exist try again'})
        if emailAlreadyExist(email):
            raise serializers.ValidationError({'email' : 'email already exist'})

        return attrs
    
    def create(self, validated_data):
        password = validated_data.get('password')
        username = validated_data.get('username')
        email    = validated_data.get('email')
        first_name= validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        try:
            user = User.objects.create_user(
                username = username,
                email = email,
                password = password,
                last_name = last_name,
                first_name=first_name
            )
            user.save()
        except ValidationError as e:
            raise serializers.ValidationError(f'{e}')
        
        return user


class UserSerializerForUpdate(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']
    def validate(self, attrs):
        username = attrs.get('username')
        email = attrs.get('email')
        if usernameAlreadyExist(username):
            raise serializers.ValidationError({'error' : 'username already exist try again'})
        if emailAlreadyExist(email):
            raise serializers.ValidationError({'error' : 'email already exist'})
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        # Perform the partial update
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        # Save the updated instance
        instance.save()

        return instance

