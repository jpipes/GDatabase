from django.urls import path
from . import views


urlpatterns = [
    path('', views.pinball_list, name='pinball_list'),
    path('repair_log/<int:pk>/', views.repair_list, name='repair_list'),
    path('repair_log_instance/<pk>/', views.repair_list_instance, name='repair_list_instance'),
    path('pinball/', views.pinball_list, name='pinball_list'),
    path('pinball/detail/<int:pk>/', views.pinball_detail, name='pinball_detail'),
    path('company/<int:pk>/', views.company_detail, name='company_detail'),
    path('year_detail/<int:pk>/', views.year_detail, name='year_detail'),
    path('location_detail/<int:pk>/', views.location_detail, name='location_detail'),
    path('pinball/new/', views.pinball_new, name='pinball_new'),
    path('company/new/', views.company_new, name='company_new'),
    path('location/<location_id>/', views.location_edit, name='location_edit'),
    path('locations/new/', views.location_new, name='location_new'),
    path('repair/add/<pinball_id>/', views.repair_new, name='repair_new')


]

