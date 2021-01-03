from django.db import models


# Create your models here.

# Le profile lié à la position
from django.http import QueryDict
from django.utils import timezone


class Profile(models.Model):
    name = models.CharField(default='profile', max_length=100, primary_key=True)
    battery = models.FloatField(default=0.0)

    def __str__(self):
        return f'Profil : [{self.name}] reste {self.battery}% de batterie'


# Une position récupérée grâce à l'appli GPSLogger (https://gpslogger.app/)
# http://{URL}}/api/positions/?
# latitude=%LAT
# &longitude=%LON
# &date_time=%TIME
# &speed=%SPD
# &profile=%PROFILE
# &battery=%BATTERY
# &serial=%SER
# &android_id=%AID
# &altitude=%ALT
# &precision=%ACC
class Position(models.Model):
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    date_time = models.DateTimeField(auto_now=False, default=timezone.now)
    speed = models.FloatField(default=0.0)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
    battery = models.FloatField(default=0.0)
    serial = models.CharField(default='0000', max_length=50)
    android_id = models.CharField(default='0000', max_length=50)
    altitude = models.FloatField(default=0.0)
    precision = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.date_time} : {self.profile.__str__()} [{self.longitude} {self.latitude}]'
