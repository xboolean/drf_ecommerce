from rest_framework import permissions

class ProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        return request.user.is_superuser
    