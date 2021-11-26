from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import CustomerUser
from .serializers import CustomerUserSerializer
from django.http import HttpResponse

# PRECISO CRIAR A CAPTURA DA QUANTIDADE DE ACESSOS PELO PLANO FORNECIDO PARA PARCEIRO

@api_view(['GET', 'POST'])
def auth(request):

    if request.method == 'GET':

        try:
            # adcionar log
            customer = CustomerUser.objects.get(username = request.GET.get('username'))
            if customer.status == '1':
                return HttpResponse('5_acessos', status=status.HTTP_200_OK)
            else:
                return HttpResponse('5_acessos', status=status.HTTP_401_UNAUTHORIZED)
        
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

            customer = CustomerUser.objects.get(username = data['username'], password = data['password'])
            if customer.status == '1':
                return HttpResponse('5_acessos', status=status.HTTP_200_OK)
            else:
                return HttpResponse('5_acessos', status=status.HTTP_401_UNAUTHORIZED)

        except CustomerUser.MultipleObjectsReturned as e:
            # adcionar log
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        except CustomerUser.DoesNotExist:
            # adcionar log
            return Response(status=status.HTTP_404_NOT_FOUND)


