from django.db import models

# Create your models here.

class ClubRep(models.Model):
    f_name = models.CharField(max_length=200, null=True)
    l_name = models.CharField(max_length=200, null=True)
    date_of_birth = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

class Club(models.Model):
    club_rep = models.ForeignKey(ClubRep, null=True, on_delete=models.SET_NULL)
    club_name = models.CharField(max_length=200, null=True)
    adress_details = models.CharField(max_length=200, null=True)
    contact_details = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.club_name}"

class Films(models.Model):
    film_name = models.CharField(max_length=200, null=True)
    film_length = models.CharField(max_length=200, null=True)
    ticket_price = models.FloatField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.film_name}"

class Booking(models.Model):
    BLOCK_TICKETS = ((10,10),(20,20),(30,30),(40,40),(50,50))

    club_rep = models.ForeignKey(ClubRep, null=True, on_delete=models.SET_NULL)
    film = models.ForeignKey(Films, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    num_of_block_tickets = models.IntegerField(null=True, choices=BLOCK_TICKETS)

    def calculate_price(self):
        total_price = self.num_of_block_tickets * self.film.ticket_price
        return total_price - total_price * 0.15

    def __str__(self):
        return f"{self.club_rep.f_name} {self.club_rep.l_name} {self.film.film_name} {self.num_of_block_tickets} {self.calculate_price()}"

