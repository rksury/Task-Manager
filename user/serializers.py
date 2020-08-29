from django.contrib.auth import authenticate
from django.utils.translation import ugettext as _
from django.core import exceptions

from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings

from user.models import User, Detail

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email'
    password_field = 'password'

    def validate(self, attrs):

        password = attrs.get(self.password_field)
        user_obj = User.objects.filter(email__iexact=attrs.get(self.username_field)).first()
        if user_obj is not None:
            credentials = {
                'username': user_obj.username,
                'password': password

                # self.password_field: attrs.get(self.password_field),
            }
            if all(credentials.values()):
                user = authenticate(username=user_obj.username, password=password)

                if user:
                    if not user.is_active:
                        msg = _('user account is Not activate yet, Contact owner to activate.')
                        raise serializers.ValidationError(msg)

                    payload = jwt_payload_handler(user)

                    return {
                        'token': jwt_encode_handler(payload),
                        'user': user
                    }
                else:
                    msg = _('Unable to log in with provided credentials.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Must include "{username_field}" and "password".')
                msg = msg.format(username_field=self.username_field)
                raise serializers.ValidationError(msg)
        else:
            msg = _('unable to login with provided credentials.')
            raise serializers.ValidationError(msg)


class UserPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'address', 'email']


class UserGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'address']


class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    mobile_number = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, max_length=32)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError('password and confirm password is not matched.')
        attrs.pop('confirm_password')
        return attrs

    def validate_password(self, value):
        if value:
            errors = dict()
            try:
                from django.contrib.auth.password_validation import validate_password
                validate_password(password=value, user=User)
            except exceptions.ValidationError as err:
                errors['password'] = list(err.messages)
                raise serializers.ValidationError(err)

        return value

    def create_user(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()

    def save(self, **kwargs):
        super().save()


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Detail
        fields = ['id', 'user', 'address']


class UserDetailGetSerializer(serializers.ModelSerializer):
    user = UserGetSerializer()

    class Meta:
        model = Detail
        fields = ['id', 'user', 'address']
