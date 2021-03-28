from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fact
from .serializers import FactSerializer
import random


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


@api_view(['GET'])
def fact_random(request):
    facts = Fact.objects.all()
    random_fact = random.choice(facts)
    serializer = FactSerializer(random_fact, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def fact_create(request):
    serializer = FactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def fact_update(request, pk):
    fact = Fact.objects.get(id=pk)
    serializer = FactSerializer(data=request.data, instance=fact)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def fact_delete(request, pk):
    fact = Fact.objects.get(id=pk)
    fact.delete()
    return Response('Fact deleted successfully!')
