from employee.models import Department, Role, Employee
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


# To check the validation of any partiucular field we can use the validate_<field_name> method and this checking is done on SERIALIZER LEVEL , so this checking is done before saving the data to the database


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name', 'location']

    def validate_name(self, value):
        dept_id = self.instance.id if self.instance else None

        if Department.objects.filter(name__iexact=value).exclude(id=dept_id).exists():
            raise serializers.ValidationError("Such department name already exists.")

        return value




class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'title', 'description']


    def validate_title(self, value):
        role_id = self.instance.id if self.instance else None

        if Role.objects.filter(title__iexact=value).exclude(id=role_id).exists():
            raise serializers.ValidationError("Such role title already exists.")

        return value




class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'position', 'department', 'role']




# Check on the both level which means ke we need to check on both the applcation level and on the database level also

'''
IMP THING WHILE CHECKING 

Always remember that we need to make the checks on the both level application level and on the database level
and in the application level on serializer level we can do that by using the validate_<field_name> method

so if we want to check that the department name should be unique so we can do that by using the validate_name method and that field name is "name" so we can use validate_name method to check that the department name should be unique


'''

