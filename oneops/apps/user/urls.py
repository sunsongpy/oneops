from rest_framework.routers import SimpleRouter

from .views import *


router = SimpleRouter(trailing_slash=False)
router.register('users', UserApi)
router.register('roles', RoleApi)
router.register('menus', MenuApi)


urlpatterns = [
    *router.urls
]