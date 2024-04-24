from rest_framework import serializers
from .models import *

class DavlatSerializers(serializers.Serializer):
    class Meta:
        model = Davlat
        fields = '__all__'

class ClubSerializers(serializers.Serializer):
    class Meta:
        model = Club
        fields = '__all__'

class PlayerSerializers(serializers.Serializer):
    class Meta:
        model = Player
        fields = '__all__'

class TransferSerializers(serializers.Serializer):
    class Meta:
        model = Transfer
        fields = '__all__'



