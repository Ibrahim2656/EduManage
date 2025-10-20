from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.course_list, name='course_list'),
    path('add/', views.course_add, name='course_add'),
    path('edit/<str:code>/', views.course_edit, name='course_edit'),
    path('delete/<str:code>/', views.course_delete, name='course_delete'),
]
