from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apis.serializers import UserSerializer, GroupSerializer
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html')


class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewwe or edited.
    '''
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows groups to be viewed or edited
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    



# Create your views here.
