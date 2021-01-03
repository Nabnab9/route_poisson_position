from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
router.register(r'positions', views.PositionViewSet)
router.register(r'profiles/(?P<profile_name>.+)/positions', views.ProfilePositionViewSet, 'profile-positions')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
