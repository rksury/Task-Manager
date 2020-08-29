from rest_framework.response import Response

from rest_framework import status

from .serializers import UserPutSerializer, CustomJWTSerializer, UserGetSerializer, UserRegisterSerializer

from user.models import User


def login(data):
    ser = CustomJWTSerializer(data=data)
    if ser.is_valid():
        user = ser.object.get('user')
        token = ser.object.get('token')
        data = auth_payload(user, token)
        return Response(data, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(ser.errors, status=status.HTTP_401_UNAUTHORIZED)


def auth_payload(user, token):
    data = {
        'token': token,
        'username': user.username,
        'email': user.email,
        'id': user.id,
        'detail': user.detail,
    }
    return data


def register_user(data):
    ser = UserRegisterSerializer(data=data)
    if ser.is_valid():
        ser.save()
        user = ser.instance
        user.set_password(ser.validated_data['password'])
        user.save()
        user_ser = UserGetSerializer(user)
        return Response(user_ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


def update_user(user, user_id, data):
    if user.is_superuser is False:
        user_id = user.id
    try:
        user_update = User.objects.get(id=user_id)
        serializer = UserPutSerializer(user_update, data=data, context={'user': user})
        if serializer.is_valid():
            user_updated = serializer.save()
            get_serializer = UserGetSerializer(user_updated, many=False)
            return Response(get_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except User.DoesNotExist:
        return Response({'error': 'user_not_exists'}, status=status.HTTP_404_NOT_FOUND)


def delete_user(user_id):
    try:
        target_user = User.objects.get(id=user_id)
        target_user.delete()
        return Response({'Message': 'user deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'user_not_exists'}, status=status.HTTP_404_NOT_FOUND)


def get_user(user_id):
    if user_id:
        try:
            target_user = User.objects.get(id=user_id)
            serializer = UserGetSerializer(target_user, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'user_not_exists'}, status=status.HTTP_404_NOT_FOUND)
    else:
        target_user = User.objects.all()
        serializer = UserGetSerializer(target_user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

