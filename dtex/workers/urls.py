from django.urls import path
from . import views

urlpatterns = [
    path('', views.worker_list, name='worker_list'),
    path('create/', views.worker_create, name='worker_create'),
    path('<int:pk>/update/', views.worker_update, name='worker_update'),
    path('<int:pk>/delete/', views.worker_delete, name='worker_delete'),

    path('<int:worker_id>/activities/', views.activity_list, name='activity_list'),
    path('<int:worker_id>/activities/create/', views.activity_create, name='activity_create'),
    path('<int:worker_id>/activities/<int:pk>/update/', views.activity_update, name='activity_update'),
    path('<int:worker_id>/activities/<int:pk>/delete/', views.activity_delete, name='activity_delete'),
    
]
