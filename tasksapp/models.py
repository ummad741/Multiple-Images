from django.db import models
import os
# Create your models here.

class House(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    description = models.TextField(null=True)
    description = models.CharField(max_length=64,null=True)
    area = models.FloatField(null=True)
    number_of_rooms = models.IntegerField(null=True)

    parking = models.BooleanField(default=False)
    pets = models.BooleanField(default=False)
    toilets = models.BooleanField(default=False)
    bathroom = models.BooleanField(default=False)

    def __str__(self):
        return self.description[:10] + "  " + str(self.id)  

class HouseImage(models.Model):
    house = models.ForeignKey(House, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='house_images')

    def __str__(self):
        return f'{self.house.id}-housening rasmi. id{self.id}'
    def delete(self):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
