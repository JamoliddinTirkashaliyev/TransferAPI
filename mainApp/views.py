from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

class DavlatModelViewSet(ModelViewSet):
    queryset = Davlat.objects.all()
    serializer_class = DavlatSerializers


class ClubModelViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializers

    @action(detail=True, methods=['get'])
    def playerlar(self, request, pk):
        club = self.get_object()
        playerlar = Player.objects.filter(club=club)
        serializer = ClubSerializers(playerlar, many=True)
        return Response(serializer.data)


class PlayerModelViewSet(ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializers

class TransferModelViewSet(ModelViewSet):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializers