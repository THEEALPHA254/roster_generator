from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MemberViewSet, RoleViewSet, RosterViewSet

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'rosters', RosterViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
