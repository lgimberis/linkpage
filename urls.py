
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers

from . import views

# Serializers define the API representation.

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('links', views.LinkViewSet, basename="link")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('is-authed', views.is_authenticated, name='is-authed'),
]
