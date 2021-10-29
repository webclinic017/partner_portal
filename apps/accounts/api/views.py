from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import CustomerUser
from .serializers import CustomerUserSerializer


@api_view(['GET', 'POST'])
def auth(request):

    if request.method == 'GET':
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if request.method == 'POST':
        data = request.data
        if CustomerUser.objects.filter(username = data['username'], password = data['password']).count() >= 1:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)