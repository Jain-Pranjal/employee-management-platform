from django.shortcuts import render
from rest_framework import mixins, viewsets
from employee.models import Employee, Department, Role
from employee.serializer import EmployeeSerializer, DepartmentSerializer, RoleSerializer
from rest_framework.permissions import AllowAny


class EmployeeViewSet(mixins.CreateModelMixin
                        , mixins.RetrieveModelMixin
                        , mixins.UpdateModelMixin
                        , mixins.DestroyModelMixin
                        , mixins.ListModelMixin
                        ,viewsets.GenericViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [AllowAny]



class DepartmentViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [AllowAny]



class RoleViewSet(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [AllowAny]


