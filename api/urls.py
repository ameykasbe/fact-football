from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('fact-list/', views.fact_list, name='fact-list'),
    path('fact-detail/<str:pk>/', views.fact_detail, name='fact-detail'),
    path('fact-create/', views.fact_create, name='fact-create'),
    path('fact-update/<str:pk>/', views.fact_update, name='fact-update'),
    path('fact-delete/<str:pk>/', views.fact_delete, name='fact-delete')
]
