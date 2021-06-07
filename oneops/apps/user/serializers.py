from rest_framework import serializers

from .models import User, Menu, Role


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'roles', 'date_joined', 'is_active', 'is_superuser', 'last_login')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

