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
    restorent=models.CharField(max_length=30)
    name= models.CharField(max_length=20)
    details= models.CharField(max_length=60)
    restorentImg=models.ImageField(upload_to='locations/', null=True)
    location= models.ForeignKey('Location', on_delete=models.CASCADE, null='True', blank=True)

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
       restos=cls.objects.order_by('location')
       return restos
    @classmethod
    def get_resto(cls,id):
       resto = cls.objects.get(id=id)
       return resto
    @classmethod
    def search_resto(cls,search_term):
        locations= cls.objects.filter(location__name__icontains=search_term)
        return locations

    class Meta:
        ordering = ['name']

