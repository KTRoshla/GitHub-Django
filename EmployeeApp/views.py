
from sre_constants import CATEGORY_UNI_DIGIT
from tkinter.messagebox import RETRY
from unittest import registerResult
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
# Create your views here.

from EmployeeApp.models import MasterCategory,MasterCategoryValues
from EmployeeApp.serializers import MasterCategorySerializer, MasterCategoryValuesSerializer

@csrf_exempt
def masterCategoryApi(request,id=0):
    if request.method=='GET':
        mastercategories = MasterCategory.objects.all()
        mastercategories_serializer = MasterCategorySerializer(mastercategories,many=True)
        return JsonResponse(mastercategories_serializer.data,safe=False)
    elif request.method=='POST':
        mastercategory_data=JSONParser().parse(request)
        mastercategory_serializer=MasterCategorySerializer(data=mastercategory_data)
        if mastercategory_serializer.is_valid():
            mastercategory_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        mastercategoryUpdate = JSONParser().parse(request)
        mastercategory = MasterCategory.objects.get(CatID=mastercategoryUpdate['CatID'])
        mastercategory_serializer = MasterCategorySerializer(mastercategory,data=mastercategoryUpdate)
        if mastercategory_serializer.is_valid():
            mastercategory_serializer.save()
            return JsonResponse("Updated Succesfully",safe=False)
        return JsonResponse("Failed to Update",safe=False) 
    elif request.method=='DELETE':
        mastercategoryDelete=MasterCategory.objects.get(CatID=id)
        mastercategoryDelete.delete()
        return JsonResponse("Deleted Successfully",safe=False)  