from rest_framework import permissions

class OrderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return request.user.is_staff
        if view.action in ['create', 'update', 'partial_update', 'destroy']:
            return request.user.is_authenticated
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return obj == request.user or request.user.is_staff