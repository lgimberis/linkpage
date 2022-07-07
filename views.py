from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse

import json, ast

from .serializers import LinkSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Link
from .forms import LinkForm

# ViewSets define the view behavior.
class LinkViewSet(viewsets.ModelViewSet):
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Link.objects.filter(owner=self.request.user)
        else:
            return Link.objects.filter(owner__is_staff=True)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)