from django.db import models
from django.contrib.gis.db import models as gis_models
# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()
from django.conf  import settings
class Construction(models.Model):
    shape=gis_models.MultiPolygonField(srid=4326)
    name=models.CharField(max_length=255)
    area=models.IntegerField()
    num_of_required_col=models.IntegerField()
    num_of_finished_col=models.IntegerField()


    def __str__(self):
        return ('Building {} with area {}'.format(self.name,self.area))


class Engineer(models.Model):
    place=gis_models.PointField(srid=4326)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    section=models.CharField(max_length=255)
    years_of_experience=models.IntegerField()
    age=models.IntegerField()

    def __str__(self):
        return (self.user.username)

class Cement_Supply(models.Model):
    construction=models.ForeignKey(Construction,on_delete=models.CASCADE,
                                           related_name='cement_supplies')
    date=models.DateTimeField()
    weight=models.IntegerField()

    def __str__(self):
        return ('The {} was transferred to {} on {}'.format(self.weight,
                                            self.construction.name,self.date))

class Water_Supply(models.Model):
    construction=models.ForeignKey(Construction,on_delete=models.CASCADE,
                                         related_name='water_supplies')
    date=models.DateTimeField()
    nuumber_of_cars=models.IntegerField()

    def __str__(self):
        return 'The {} was transferred to {} on {}'.fromat(self.nuumber_of_cars,
                                               self.construction.name,self.date)

class Brick_Supply(models.Model):
    construction=models.ForeignKey(Construction,on_delete=models.CASCADE,
                                             related_name='brick_supplies')
    date=models.DateTimeField()
    nuumber_of_cars=models.IntegerField()

    def __str__(self):
        return 'The {} was transferred to {} on {}'.fromat(self.nuumber_of_cars,
                                               self.construction.name,self.date)
