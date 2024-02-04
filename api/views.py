from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from mobile.models import Mobiles
from api.serializer import MobileSerializer


# Create your views here.

#api for creating and listing all mobiles

class MobileListCreateView(APIView):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        #to deserialize qs
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        #serialization
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
         serializer.save()
         return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
#localhost:8000/api/mobiles/{id}   
class MobileDetailUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(qs)
        return Response(data=serializer.data)
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        mobile_object=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(data=request.data,instance=mobile_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    
    def delete(self,request,*Args,**kwargs):
        id=kwargs.get('pk')
        Mobiles.objects.get(id=id).delete()
        return Response(data={"message":"mobile delete view"})
    

class MobileViewSetView(viewsets.ViewSet):
    def list(self,request,*Args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(qs)
        return Response(data=serializer.data)
    

    def create(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data) #serialization
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        mobile_object=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(data=request.data,instance=mobile_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Mobiles.objects.get(id=id).delete()
        return Response(data={"message":"data deleted successfully"})