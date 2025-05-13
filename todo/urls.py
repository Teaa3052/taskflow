from django.urls import path
from . import views

urlpatterns = [
    # To-Do zadaci
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_todo, name='add_todo'),
    path('edit/<int:pk>/', views.edit_todo, name='edit_todo'),
    path('delete/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('toggle/<int:pk>/', views.toggle_completed, name='toggle_completed'),

    # Autentikacija
    path('register/', views.register, name='register'),
    path('logout/', views.custom_logout, name='logout'),

    # Liste zadataka (kategorije)
    path('add-list/', views.add_list, name='add_list'),
    path('edit-list/<int:pk>/', views.edit_list, name='edit_list'),
    path('delete-list/<int:list_id>/', views.delete_list, name='delete_list'),
]
