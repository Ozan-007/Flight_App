from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsStuffOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
                    )
