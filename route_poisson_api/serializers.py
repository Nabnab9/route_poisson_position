from rest_framework import serializers

from .models import Profile, Position


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('name',
                  'battery',
                  )


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id',
                  'longitude',
                  'latitude',
                  'date_time',
                  'speed',
                  'profile',
                  'battery',
                  'serial',
                  'android_id',
                  'altitude',
                  'precision',
                  )

    def to_representation(self, instance):
        self.fields['profile'] = ProfileSerializer(read_only=True)
        return super(PositionSerializer, self).to_representation(instance)

