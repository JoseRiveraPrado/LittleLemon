from django.db import models

# Create your models here.
class Menu(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically increments ID
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def get_item(self):
        return f'{self.title} : {str(self.price)}'


class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # Automatically increments ID
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"Booking for {self.name} on {self.booking_date}"