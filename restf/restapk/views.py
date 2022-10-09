from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from .models import Personne 
from django.forms.models  import model_to_dict
from django.http import JsonResponse
from . serializer import PersonneSerializer
from rest_framework import generics,permissions,authentication


class DetailPersonne(generics.RetrieveAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer



@api_view(['GET'])
def query_set(request):
    obj = Personne.objects.all().order_by('?').first()
    data = {}
    if obj:   
        data = PersonneSerializer(obj).data
    return Response(data)


@api_view(['POST'])
def addData(request):
    data = request.data 
    serializer = PersonneSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    

class CreatePersonne(generics.CreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer


class UpdatePersonne(generics.UpdateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    lookup_field='pk'
    
class Createlist(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    authentication_classes = [authentication.SessionAuthentication]