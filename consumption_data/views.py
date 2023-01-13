from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Energy_consumption
from .serializers import EnergyDataSerializer


class EnergyViewSet(viewsets.ViewSet):
    def list(self, request):
        energy_comsumption = Energy_consumption.objects.all()
        serializer = EnergyDataSerializer(energy_comsumption, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EnergyDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        energy_comsumption = Energy_consumption.objects.get(id=pk)
        serializer = EnergyDataSerializer(energy_comsumption)
        return Response(serializer.data)

    def retrieve_by_user(self, request, user_id=None):
        energy_comsumption = Energy_consumption.objects.all().filter(user_id=user_id)
        serializer = EnergyDataSerializer(energy_comsumption, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        energy_comsumption = Energy_consumption.objects.get(id=pk)
        energy_comsumption.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
