
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Link

# Serializers define the API representation.
class LinkSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Link
        fields = ['url', 'id', 'name', 'link_url', 'description', 'owner']
