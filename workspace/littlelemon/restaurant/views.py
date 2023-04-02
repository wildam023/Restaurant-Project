from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from .models import Menu
from .serializers import MenuSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer