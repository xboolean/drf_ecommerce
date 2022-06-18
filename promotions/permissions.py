from rest_framework import permissions

class PromotionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ['list', 'create', 'update', 'partial_update', 'destroy']:
            return request.user.is_staff
        else:
            return False
    
    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff:
            return False
        else:
            return True