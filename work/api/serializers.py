from rest_framework import serializers
from . import models

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = 'Employee'
        fields = ('eid','ename','eemail','econtact','creation_time')
