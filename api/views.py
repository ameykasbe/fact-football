from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fact
from .serializers import FactSerializer


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


@api_view(['GET'])
def fact_list(request):
    facts = Fact.objects.all()
    serializer = FactSerializer(facts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def fact_detail(request, pk):
    fact = Fact.objects.get(id=pk)
    serializer = FactSerializer(fact, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def fact_create(request):
    serializer = FactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
