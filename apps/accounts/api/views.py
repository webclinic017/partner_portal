from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import CustomerUser
from .serializers import CustomerUserSerializer
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def auth(request):

    if request.method == 'GET':

        try:
            # adcionar log
            CustomerUser.objects.get(username = request.GET.get('username'))
            return HttpResponse('5_acessos', status=status.HTTP_200_OK)
        
        except CustomerUser.MultipleObjectsReturned as e:
            # adcionar log
            # tratar clientes de diferentes provedores que possuem mesmo username
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        except CustomerUser.DoesNotExist:
            # adcionar log
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':

        try:
            # adcionar log
            data = request.data
            CustomerUser.objects.get(username = data['username'], password = data['password'])
            return HttpResponse('5_acessos', status=status.HTTP_200_OK)
        
        except CustomerUser.MultipleObjectsReturned as e:
            # adcionar log
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        except CustomerUser.DoesNotExist:
            # adcionar log
            return Response(status=status.HTTP_404_NOT_FOUND)


