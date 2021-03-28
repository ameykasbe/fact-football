from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/fact-list/',
        'Detail': '/fact-detail/<str:pk>',
        'Create': '/fact-create/',
        'Update': '/fact-update/<str:pk>',
        'Delete': '/fact-delete/<str:pk>',
    }
    return Response(api_urls)
