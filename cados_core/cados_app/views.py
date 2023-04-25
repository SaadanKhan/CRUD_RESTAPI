from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Advocate,Comapny
from .serializers import AdvocateSerializer,CompanySerializer,ValidateSerializer
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# User must be Authenticated to access this
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def advocate_list(request):
    
    # 127.0.0.1:8000/advocate_list/?query=ahab
    if request.method == 'GET':
        query = request.GET.get('query')
        if query == None:
            query = ''

        # Filtering data by name OR bio
        data = Advocate.objects.filter(
            Q(username__icontains=query) | Q(bio__icontains=query))
        
        serializer = AdvocateSerializer(data, many = True) 
        return Response(serializer.data)
    
    if request.method == 'POST':
        advocate = Advocate.objects.create(
        username = request.data['username'],
        bio = request.data['bio']
        )
        serializer = AdvocateSerializer(advocate,many = False)
        return Response(serializer.data)


class AdvocateDetail(APIView):  
    def get_object(self,username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse('Does not exist !')

    def get(self, request, name):
        data = self.get_object(name)
        serializer = AdvocateSerializer(data, many = False)
        return Response(serializer.data)
    
    def put(self, request, name):
        data = self.get_object(name)
        data.username = request.data['username']
        data.bio = request.data['bio']
        data.save()
        serializer = AdvocateSerializer(data, many = False)
        return Response(serializer.data)

    def delete(self, request, name):
        data = self.get_object(name)
        data.delete()
        return Response('Deleted')                 

@api_view(['GET'])
def company_list(request):
    company = Comapny.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)



# @api_view(['GET','PUT','DELETE'])
# def advocate_detail(request,name):
    # data = Advocate.objects.get(username = name)
    
    # if request.method == 'GET':
    #     serializer = AdvocateSerializer(data, many = False)
    #     return Response(serializer.data)
    
    # if request.method == 'PUT':
    #     data.username = request.data['username']
    #     data.bio = request.data['bio']
    #     data.save()
    #     serializer = AdvocateSerializer(data, many = False)
    #     return Response(serializer.data)

    # if request.method == 'DELETE':
    #     data.delete()
    #     return Response('Deleted')       