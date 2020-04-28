from .models import Network

class ChangeModel(object):
    def has_permission(self, request,view):
        return True
