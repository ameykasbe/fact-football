from django.urls import path
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('fact-list/', views.fact_list, name='fact-list'),
    path('fact-detail/<str:pk>', views.fact_detail, name='fact-detail')
]
