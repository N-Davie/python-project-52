
from django.urls import path
from . import views


urlpatterns = [
   path('', views.IndexView.as_view(), name='index'),
   path('login/', views.UserLoginView.as_view(), name='signin'),
   path('logout/', views.UserLogoutView.as_view(), name='signout'),
]
