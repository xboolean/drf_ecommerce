from rest_framework import permissions

class ProductPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        if view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff:
            return False
        else:
            return True

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class AdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or request.user.is_staff)