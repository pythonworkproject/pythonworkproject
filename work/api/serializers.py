from rest_framework import serializers
from employee_app.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('eid','ename','eemail','econtact','creation_time')
