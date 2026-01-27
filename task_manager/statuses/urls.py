from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('statuses/', views.StatusListView.as_view(), name='status-list'),
    path('statuses/create/', views.StatusCreateView.as_view(), name='status-create'),
    path('statuses/<int:pk>/update/', views.StatusUpdateView.as_view(), name='status-update'),
    path('statuses/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status-delete'),
]
