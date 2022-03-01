from rest_framework import serializers
from UserApp.models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['UserId',
                    'UserName',
                    'UserEmail',
                    'UserFirstName',
                    'UserLastName',
                    'DateOfBirth',
                    'PhotoFileName',
                    'password']

    def validate(self, attrs):
        email = attrs.get('UserEmail', '')
        username = attrs.get('UserName', '')

        if not username.isalnum():
            raise serializers.ValidationError('Username should only contain alphanumeric characters')
        return attrs
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

'''
class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Style
        fields = ('StyleId',
                    'StyleName')'''

