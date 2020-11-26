from rest_framework import serializers
from user_center import models


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Permission
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Department
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    dept = DepartmentSerializer()

    class Meta:
        model = models.User
        fields = '__all__'
