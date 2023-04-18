from .utils import *
from .models import Pokemon
from .serializers import PokemonSerializer
from rest_framework.decorators import api_view

@api_view(['GET'])
def pokemon_list(request):
    if request.method == 'GET':
        data = Pokemon.objects.all()

        return response(data=PokemonSerializer(data, many=True).data, status=status.HTTP_200_OK)

    return response(error="Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
@api_view(['POST'])
def pokemon_create(request):
    if request.method == 'POST':
        data = Pokemon.objects.create(name=request.data['name'], type=request.data['type'], height=request.data['height'], weight=request.data['weight'])
        data.save()
        return response(data=PokemonSerializer(data).data, status=status.HTTP_201_CREATED)

    return response(error="Method not allowed", status=status.HTTP_405_METHOD_NOT_ALLOWED)