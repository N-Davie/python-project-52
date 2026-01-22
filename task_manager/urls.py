from django.contrib import admin
from django.urls import path, include
from task_manager_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),  # стартовая страница
    path('', include('task_manager_app.urls')),  # маршруты для статусов и пользователей
]
