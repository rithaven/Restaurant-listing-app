from django.db import models

# Create your models here.
class Location(models.Model):
    name= models.Charfield(max_length=30)
     
    def __str__(self):
        return self.name
    def saveLocation(self):
        self.save()

    def deleteLocation(self):
        Location.objects.filter(id = self.pk).delete()
    
    def updateLocation(self, **kwargs):
        self.objects.filter(id= self.pk).update(**kwargs)
    