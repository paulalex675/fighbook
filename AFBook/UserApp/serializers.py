from rest_framework import serializers
from UserApp.models import Users, Styles

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('UserId',
                    'UserUserName',
                    'UserFirstName',
                    'UserLastName',
                    'DateOfBirth',
                    'PhotoFileName')

class StyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Styles
        fields = ('StyleId',
                    'StyleName')

