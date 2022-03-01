
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status, views, permissions
from .models import User
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http.response import JsonResponse
from UserApp.serializers import RegisterSerializer

from .models import User
from .serializers import RegisterSerializer

from django.core.files.storage import default_storage



# Create your views here.

class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


'''class StyleList(APIView):
    def get(self, request, format=None):
        styles = Styles.objects.all()
        styles_serializer = StyleSerializer(styles, many=True)
        return JsonResponse(styles_serializer.data, safe=False)

    def post(self, request, format=None):
        style_data = JSONParser().parse(request)
        style_serializer = StyleSerializer(data=request.data)
        if style_serializer.is_valid():
            style_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

class StyleDetail(APIView):
    def get_object(self, id):
        try:
            return Styles.objects.get(id=id)
        except Styles.DoesNotExist:
            raise HttpResponse(status=404)

    def get(self, request, id, format=None):
        style = self.get_object(id)
        style_serializer = StyleSerializer(style)
        return JsonResponse(style_serializer.data, safe=False)

    def put(self, request, id, format=None):
        style_data = JSONParser().parse(request)
        style = Styles.objects.get(StyleId = style_data['StyleId'])
        style_serializer = StyleSerializer(style, data=style_data)
        if style_serializer.is_valid():
            style_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    def delete(self, request, id, format=None):
        style = Styles.objects.get(StyleId = id)
        style.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

class UserList(APIView):
    def get(self, request, format=None):
        user = User.objects.all()
        users_serializer = UserSerializer(user, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    def post(self, request, format=None):
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

class UserDetail(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            raise HttpResponse(status=404)

    def get(self, request, id, format=None):
        user = self.get_object(id)
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data, safe=False)

    def put(self, request, id, format=None):
        user_data = JSONParser().parse(request)
        user = User.objects.get(UserId = user_data['UserId'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    def delete(self, request, id, format=None):
        user = User.objects.get(UserId = id)
        user.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)'''