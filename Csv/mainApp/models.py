from django.db import models

# Create your models here.
class Item (models.Model):
    name = models.TextField()
    description = models.TextField()
    code = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    vendor = models.TextField()
    

    
    def __str__(self):
        return self.name

