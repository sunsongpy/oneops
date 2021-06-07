from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class UserApi(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MenuApi(ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class RoleApi(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



