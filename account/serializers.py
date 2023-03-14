from rest_framework import serializers
from account.models import Users,user_details
import re 


class UserRegistrationserializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=Users
        fields=['email','password','password2']
        extra_kwargs={'password':{'write_only':True}}
    def validate(self, data):
        password=data.get('password')
        if password != data.get('password2'):
            raise serializers.ValidationError('The Password and the confirm password does not Match')
        return data
    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)

    
class Userloginserializer(serializers.ModelSerializer):
    email= serializers.CharField(max_length=255)
    class Meta:
        model=Users
        fields=['email','password']

class GetUserDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields=['First_Name','Middle_Name','Last_Name','date_of_birth','Gender']

class UserProfileSerializer(serializers.ModelSerializer):
    #Users= serializers.SlugRelatedField(many=True,read_only=True,slug_field='email')
    Users = GetUserDetailsSerializers(many=True,read_only=True)
    #print(abc)
    class Meta:
        model = Users
        fields = ['email','is_admin','Users']

class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=user_details
        fields=['First_Name','Middle_Name','Last_Name','date_of_birth','Gender']
    def validate(self, attrs):
        return attrs
    def create(self, validated_data):
        print(validated_data.get('users', None))
        users = validated_data.get('users', None)
        # my code
        data = user_details.objects.create(**validated_data)
        return data
