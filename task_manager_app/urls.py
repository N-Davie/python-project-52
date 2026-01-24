from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from task_manager_app.views import (
    user_views,
    status_views,
    task_views,
    label_views,
    misc_views
)
from task_manager_app.views import home

urlpatterns = [
    # маршруты для пользователей
    path('users/', user_views.UserListView.as_view(), name='user-list'),
    path('users/create/', user_views.UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', user_views.UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', user_views.UserDeleteView.as_view(), name='user-delete'),

    # маршруты для статусов
    path('statuses/', status_views.StatusListView.as_view(), name='status-list'),
    path('statuses/create/', status_views.StatusCreateView.as_view(), name='status-create'),
    path('statuses/<int:pk>/update/', status_views.StatusUpdateView.as_view(), name='status-update'),
    path('statuses/<int:pk>/delete/', status_views.StatusDeleteView.as_view(), name='status-delete'),

    # логин и логаут
    path('login/', LoginView.as_view(template_name='task_manager_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # маршруты для задач
    path('tasks/', task_views.TaskListView.as_view(), name='task-list'),
    path('tasks/create/', task_views.TaskCreateView.as_view(), name='task-create'),
    path('tasks/<int:pk>/', task_views.TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/update/', task_views.TaskUpdateView.as_view(), name='task-update'),
    path('tasks/<int:pk>/delete/', task_views.TaskDeleteView.as_view(), name='task-delete'),

    # маршруты для меток
    path('labels/', label_views.LabelListView.as_view(), name='label-list'),
    path('labels/create/', label_views.LabelCreateView.as_view(), name='label-create'),
    path('labels/<int:pk>/update/', label_views.LabelUpdateView.as_view(), name='label-update'),
    path('labels/<int:pk>/delete/', label_views.LabelDeleteView.as_view(), name='label-delete'),

    # тестовый маршрут для Rollbar
    path('rollbar-test/', misc_views.rollbar_test, name='rollbar-test'),
]
