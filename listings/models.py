from django.db import models
from datetime import datetime
from dealers.models import Dealer


class Listing(models.Model):
    dealer = models.ForeignKey(Dealer, on_delete=models.DO_NOTHING)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    odo = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    type = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    engine_type = models.CharField(max_length=20)
    main_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    description = models.TextField(max_length=400)

    def __str__(self):
        return f'{self.make}  {self.model}'