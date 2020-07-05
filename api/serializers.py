
from utils.Response import MyResponse
from rest_framework import serializers,exceptions

from api.models import User, Emploee


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        # fields=('username','password','real_name','sex')
        extra_kwargs = {
            'username':{
                'required':True,
                'min_length':3,
                'error_messages':{
                    'required':'用户名不能为空',
                    'min_length':'用户名至少三位'
                }
            },
            'password': {
                'required': True,
                'min_length': 6,
                'error_messages': {
                    'required': '密码不能为空',
                    'min_length': '密码至少六位'
                }
            }
        }

    # def validate_username(self, value):
    #     print(15,value)
    #     user = User.objects.filter(username=value).first()
    #     if user:
    #         raise exceptions.ValidationError('用户名已存在')
    #     return value
    def validate(self, attrs):
        uname=attrs.get('username')
        print(23,uname)
        user=User.objects.filter(username=uname).first()
        if user:
            raise exceptions.ValidationError('用户名已存在')
        print(21,attrs)
        return attrs

class EmploeeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Emploee
        fields='__all__'
        # fields=('name','salary','age','photo')

    # def validate(self, attrs):
    #     name=attrs.get('name')
    #     if 'j' in name:
    #         raise exceptions.ValidationError('姓名不符合标准')
    #     print(attrs)
    #     return attrs








