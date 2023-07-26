from rest_framework import serializers
from . import models


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Menu
        fields = "__all__"
