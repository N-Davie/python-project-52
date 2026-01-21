from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),  # список пользователей
    path('users/create/', UserCreateView.as_view(), name='user-create'),  # регистрация
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),  # редактирование
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),  # удаление
    path('login/', LoginView.as_view(template_name='task_manager_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
