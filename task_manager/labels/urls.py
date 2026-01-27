from django.urls import path
from . import views

urlpatterns = [
    path('labels/', views.LabelListView.as_view(), name='label-list'),
    path('labels/create/', views.LabelCreateView.as_view(), name='label-create'),
    path('labels/<int:pk>/update/', views.LabelUpdateView.as_view(), name='label-update'),
    path('labels/<int:pk>/delete/', views.LabelDeleteView.as_view(), name='label-delete'),
]
