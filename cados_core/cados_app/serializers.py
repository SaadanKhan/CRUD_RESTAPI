from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate,Comapny
from rest_framework import serializers
from rest_framework.response import Response

class CompanySerializer(ModelSerializer):  
    # This thing will add an extra field "employee_count" in the company serializer 
    employee_count = SerializerMethodField(read_only = True)
    class Meta:
        model = Comapny
        fields = '__all__'

    # That "employee_count" field is accessed here by the "get" keyword, and in that field we have created number of advocates, 
    def get_employee_count(self, obj):
        count = obj.advocate_set.count()
        return count


class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer() # new field
    class Meta:
        model = Advocate
        fields = ['username','bio','company']

