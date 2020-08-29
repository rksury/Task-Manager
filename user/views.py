from rest_framework.decorators import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .services import register_user, login, get_user, update_user, delete_user, add_details, get_detail, update_user_details


class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        return login(data=request.data)


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        return register_user(data=request.data)


# Create your views here.
class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user_id=None):
        if not user_id:
            user_id = request.user.pk
        return get_user(user_id)

    def put(self, request, user_id):
        return update_user(request.user, user_id, request.data)

    def delete(self, request, user_id=None):
        if not user_id:
            user_id = request.user.pk
        return delete_user(user_id)


class DetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        return add_details(request.user, request.data)

    def put(self, request, user_id):
        return update_user_details(request.user, user_id, request.data)

    def get(self, request, user_id=None):
        return get_detail(request.user, user_id)
