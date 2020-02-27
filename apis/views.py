from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apis.serializers import UserSerializer, GroupSerializer

# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows users to be viewwe or edited.
    '''
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer