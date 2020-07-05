from django.urls import path
from api import views
urlpatterns=[
    path('user/',views.UserAPIView.as_view()),
    path('user/<str:uname>',views.UserAPIView.as_view()),
    path('regist/',views.RegisterViewSet.as_view({'get':'check_uname'})),
    path('emp/',views.EmploeeGenericAPIView.as_view()),
    path('emp/<str:id>',views.EmploeeGenericAPIView.as_view())
]