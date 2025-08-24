from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManager_Or_IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # gets permission only if user is authenticated & has role of Admin or Manager
        return request.user.is_authenticated and request.user.role in ['Admin', 'Manager']
    

class IsWaiter(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Waiter'
    

class IsCashier(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'Cashier'