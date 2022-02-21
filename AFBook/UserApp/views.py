from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from UserApp.models import Styles, Users
from UserApp.serializers import UserSerializer, StyleSerializer

from django.core.files.storage import default_storage



# Create your views here.
@csrf_exempt
def styleApi(request,id=0):
    if request.method == 'GET':
        styles = Styles.objects.all()
        styles_serializer = StyleSerializer(styles, many=True)
        return JsonResponse(styles_serializer.data, safe=False)

    elif request.method == 'POST':
        style_data = JSONParser().parse(request)
        style_serializer = StyleSerializer(data=style_data)
        if style_serializer.is_valid():
            style_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        style_data = JSONParser().parse(request)
        style = Styles.objects.get(StyleId = style_data['StyleId'])
        style_serializer = StyleSerializer(style, data=style_data)
        if style_serializer.is_valid():
            style_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        style = Styles.objects.get(StyleId = id)
        style.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

@csrf_exempt
def userApi(request,id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(UserId = user_data['UserId'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!", safe=False)
        return JsonResponse("Failed to Update", safe=False)

    elif request.method == 'DELETE':
        user = Users.objects.get(UserId = id)
        user.delete()
        return JsonResponse("Deleted Successfully!", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)