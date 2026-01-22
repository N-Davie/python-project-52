from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    UserListView, UserCreateView, UserUpdateView, UserDeleteView,
    StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView,
    TaskListView, TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView,
    LabelListView, LabelCreateView, LabelUpdateView, LabelDeleteView,
    rollbar_test
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

    # маршруты для задач
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),

    # маршруты для меток
    path('labels/', LabelListView.as_view(), name='label-list'),
    path('labels/create/', LabelCreateView.as_view(), name='label-create'),
    path('labels/<int:pk>/update/', LabelUpdateView.as_view(), name='label-update'),
    path('labels/<int:pk>/delete/', LabelDeleteView.as_view(), name='label-delete'),

    # тестовый маршрут для Rollbar
    path('rollbar-test/', rollbar_test, name='rollbar-test'),
]
