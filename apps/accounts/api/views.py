from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import CustomerUser
from .serializers import CustomerUserSerializer
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def auth(request):

    if request.method == 'GET':
        
        if CustomerUser.objects.filter(username__icontains = request.GET.get('username')).count() >= 1:
            return HttpResponse('5_acessos', status=status.HTTP_200_OK)
        else:
            CustomerUser.objects.create(username = 'a', password = 'b')
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        data = request.data
        if CustomerUser.objects.filter(username__icontains = data['username'], password__icontains = data['password']).count() >= 1:
            return HttpResponse('5_acessos', status=status.HTTP_200_OK)
        else:
            CustomerUser.objects.create(username = 'a', password = 'b')
            return Response(status=status.HTTP_404_NOT_FOUND)