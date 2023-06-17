from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class CustomerUserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(email=username)
            
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None