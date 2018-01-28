from rest_framework import permissions


class HextrackCommonPermission(permissions.IsAuthenticated):
    pass


class HextrackAnonymousPermission(permissions.AllowAny):
    pass
