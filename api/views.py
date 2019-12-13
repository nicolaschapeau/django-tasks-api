from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.models import User, Task
from api.serializers import UserSerializer, TaskSerializer
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser



class UserViewSet(viewsets.ModelViewSet):
    """
    User views, will create list, retrieve, update and delete views automatically.
    """

    # Used data
    queryset = User.objects.all()
    # Used serializer
    serializer_class = UserSerializer


    def get_permissions(self):
        """
        Return permission to do a certain action
        """
        permission_classes = []

        # Everyone can create a Profile, see a profile or see all profiles.
        if self.action == 'create' or self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # If you are logged in you can edit your profile, or if you are admin.
        elif self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        # Return permissions
        return [permission() for permission in permission_classes]


class TaskViewSet(viewsets.ModelViewSet):
    """
    Tasks views
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_permissions(self):
        """
        Return permission to do a certain action
        """
        permission_classes = []

        # Everyone can create a Profile, see a profile or see all profiles.
        if self.action == 'retrieve' or self.action == 'list':
            permission_classes = [AllowAny]
        # If you are logged in you can edit your profile, or if you are admin.
        elif self.action == 'create' or self.action == 'update' or self.action == 'partial_update' or self.action == 'destroy':
            permission_classes = [IsLoggedInUserOrAdmin]

        # Return permissions
        return [permission() for permission in permission_classes]