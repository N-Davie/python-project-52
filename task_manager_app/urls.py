from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView
)

urlpatterns = [
    # маршруты для пользователей
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),

    # маршруты для статусов
    path('statuses/', StatusListView.as_view(), name='status-list'),
    path('statuses/create/', StatusCreateView.as_view(), name='status-create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(), name='status-update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name='status-delete'),

    # логин и логаут
    path('login/', LoginView.as_view(template_name='task_manager_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
