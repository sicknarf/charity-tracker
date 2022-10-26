from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

DONOS = (
    ('05', '$5'),
    ('10', '$10'),
    ('20', '$20'),
    ('50', '$50'),
)

class Donation(models.Model):
    amount = models.CharField(
        max_length = 2,
        choices = DONOS,
        default = DONOS[0][0]
    )
    donator = models.CharField(max_length=20)
    pokemon = models.CharField(max_length=20, blank=True)
    blindfolded = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_time = models.DateTimeField('date created', default=timezone.now)

    def __str__(self):
        # if self.pokemon=="":
        #     return "this is doing what you're expecting"
        return f"{self.donator} donated ${int(self.amount)}"
        # if self.completed == False:
        #     if self.blindfolded==False:
        #         return f"${self.amount} donated by {self.user}"
        #     else:
        #         return f"${self.amount} donated by {self.user} (BLINDFOLDED)"