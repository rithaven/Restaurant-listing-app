from django.db import models

# Create your models here.
class Location(models.Model):
    name= models.CharField(max_length=30)
     
    def __str__(self):
        return self.name
    def saveLocation(self):
        self.save()

    def deleteLocation(self):
        Location.objects.filter(id = self.pk).delete()
    
    def updateLocation(self, **kwargs):
        self.objects.filter(id= self.pk).update(**kwargs)
        
class Restorent(models.Model):
    restorent= models.RestorentField(upload_to = 'locations/', null = True)
    name=models.Charfield(max_length=20)
    details=models.Charfield(max_length=60)
    location=models.Foreignkey('Location', on_delete=models.CASCADE,null='True', blank=True)

    def __str__(self):
        return self.name

    def save_restorent(self):
        self.save()


    def delete_restorent(self):
        Restorent.objects.filter(id =self.pk).delete()
    def update_restorent(self,**kwargs):
        self.objects.filter(id=self.pk).update(**kwargs)
    @classmethod
    def restorent(cls):
       restos = cls.objects.all()
       return restos
    @classmethod
    def restorent_location(cls):
        restos = cls.objects.get(id=id)
        return restos
    @classmethod
    def search_resto(cls,search_term):
        locations= cls.objects.filter(location__name__icontains=search_term)
        return locations

    class Meta:
        ordering = ['name']