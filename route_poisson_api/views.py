from rest_framework.exceptions import NotFound

from rest_framework import viewsets

from .serializers import ProfileSerializer, PositionSerializer
from .models import Profile, Position


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('name')
    serializer_class = ProfileSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all().order_by('date_time')
    serializer_class = PositionSerializer

    def perform_create(self, serializer):
        print(self.request.query_params)

        params = self.request.query_params
        profile_name = params.get('profile')
        battery = float(params.get('battery')[:-3])

        try:
            profile = Profile.objects.get(name=profile_name)
            profile.battery = battery
            profile.save()
        except Profile.DoesNotExist:
            print(f"Le profil {profile_name} n'existe pas, il va être créé")
            profile = Profile.objects.create(name=profile_name, battery=battery)

        serializer.save(
            longitude=params.get('longitude'),
            latitude=params.get('latitude'),
            date_time=params.get('date_time'),
            speed=params.get('speed'),
            profile=profile,
            battery=battery,
            serial=params.get('serial'),
            android_id=params.get('android_id'),
            altitude=params.get('altitude'),
            precision=params.get('precision')
        )


class ProfilePositionViewSet(viewsets.ModelViewSet):
    serializer_class = PositionSerializer

    filterset_fields = {
        'date_time': ['gte'],
    }

    def get_queryset(self):
        profile_name = self.kwargs['profile_name']
        try:
            profile = Profile.objects.get(name=profile_name)
        except Profile.DoesNotExist:
            raise NotFound("Le profil demandé n'existe pas.")

        return Position.objects.filter(profile=profile)
