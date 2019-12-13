from django.conf.urls import url, include
from rest_framework import routers
from api.views import UserViewSet, TaskViewSet


# Router configuration
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'tasks', TaskViewSet)



# Url configuration
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]