from django.contrib import admin
from django.urls import path, include
from task_manager_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),  # стартовая страница
    path('', include('task_manager_app.urls')),  # маршруты для статусов и пользователей
    path('users/', include('users.urls')),
    path('tasks/', include('tasks.urls')),
    path('statuses/', include('statuses.urls')),
    path('labels/', include('labels.urls')),
]
