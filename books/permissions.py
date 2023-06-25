from rest_framework import permissions
from .models import Book,Page,Author

class IsReader(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author.user == request.user:
            return True
        return False