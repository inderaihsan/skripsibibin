from django.shortcuts import render
from rest_framework.decorators import api_view  
from rest_framework.response import Response 
from . models import *  
from . serializers import * 
# Create your views here. 

@api_view(['GET']) 
def init(request) : 
    return Response({'status' : 'apirunning'}) 

@api_view(['GET']) 
def get_all_pelatihan(request) : 
    fetch_query = Pelatihan.objects.all()  
    serialized = PelatihanSerializer(fetch_query, many = True).data
    return Response({'data' : serialized})