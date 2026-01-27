from django.contrib import admin
from django.urls import path, include
from task_manager.misc_views import home, rollbar_test
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    # Главная страница
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    # маршруты
    path('users/', include('task_manager.users.urls')),
    path('tasks/', include('task_manager.tasks.urls')),
    path('statuses/', include('task_manager.statuses.urls')),
    path('labels/', include('task_manager.labels.urls')),
    
    # логин и логаут
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # тестовый маршрут для Rollbar
    path('rollbar-test/', rollbar_test, name='rollbar-test'),
]
