from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpRequest


UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username: str=None, password: str=None, **kwargs: str) -> UserModel | None:
        if username is None or password is None:
            return
        
        user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).first()

        if user:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        else:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)