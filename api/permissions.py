from rest_framework import permissions



class IsLoggedInUserOrAdmin(permissions.BasePermission):
    """
    Return True if the user is logged in (User or staff)
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff


class IsAdminUser(permissions.BasePermission):
    """
    Return True if the user is Admin
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff