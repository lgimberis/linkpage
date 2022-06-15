from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

import json, ast

from .serializers import LinkSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Link
from .forms import LinkForm

# ViewSets define the view behavior.
class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
