from django.shortcuts import render
from rest_framework.response import Response

from api.models import User, Emploee
from utils.Response import MyResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin,ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin
from rest_framework.viewsets import ViewSet,ModelViewSet
from api.serializers import UserModelSerializer,EmploeeModelSerializer
# Create your views here.
class UserAPIView(APIView):

    def get(self,request,*args,**kwargs):
        uname=request.query_params['username']
        pwd=request.query_params['password']
        print(uname,pwd)
        user=User.objects.filter(username=uname,password=pwd).first()
        user_ser=UserModelSerializer(user)
        print('登陆', user_ser, type(user_ser))
        if user:
            return MyResponse(200,True,results=user_ser.data)
        return MyResponse(401,False)
    def post(self,request,*args,**kwargs):
        user_data=request.data
        user=UserModelSerializer(data=user_data)
        print('注册用户',user,type(user))
        user.is_valid(raise_exception=True)
        user.save()
        return MyResponse(200,'注册用户成功')

    def delete(self,request,*args,**kwargs):
        uname=kwargs.get('uname')
        user=User.objects.filter(username=uname)[0]
        user.delete()
        return MyResponse(200,True)



class EmploeeGenericAPIView(GenericAPIView,RetrieveModelMixin,ListModelMixin,UserAPIView,DestroyModelMixin,CreateModelMixin,UpdateModelMixin):
    queryset = Emploee.objects.all()
    serializer_class = EmploeeModelSerializer
    lookup_field = 'id'
    def get(self,request,*args,**kwargs):
        emp_id=kwargs.get('id')
        if emp_id:
            print('单查',emp_id)
            emp_ser=self.retrieve(request,*args,**kwargs)
            return MyResponse(200,True,results=emp_ser.data)
        emps_ser=self.list(request,*args,**kwargs)
        return MyResponse(200,True,results=emps_ser.data)
    def post(self,request,*args,**kwargs):

        emp_ser=self.create(request,*args,**kwargs)
        return MyResponse(200,True,results=emp_ser.data)

    def delete(self,request,*args,**kwargs):
        # emp_id=request.query_params['id']

        emp_id=kwargs.get('id')
        print('删除', emp_id)
        # emp=Emploee.objects.get(id=emp_id)
        # print(emp)
        # emp.delete()
        self.destroy(request,*args,**kwargs)
        return MyResponse('删除成功')

    def patch(self, request, *args, **kwargs):
        emp_id=kwargs.get('id')
        print('更新获取',emp_id)
        emp_ser=self.partial_update(request, *args, **kwargs)
        print(emp_ser.data)
        return MyResponse(200,True,results=emp_ser.data)

class RegisterViewSet(ViewSet):
    def check_uname(self,request,*args,**kwargs):
        uname = request.query_params['username']
        # print(77, uname)
        user=User.objects.filter(username=uname).first()
        if user:
            return MyResponse(403,False)
        return MyResponse(403, True)


