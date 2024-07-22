from django.db import models
from django.contrib.auth.models import User
from viewer.constants import REGION_CHOICES


class Event(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=40, choices=REGION_CHOICES, default='')
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user} on {self.event}'


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} registered for {self.event}'




#TODO JIRKA, udelat readme projektu, poskladat kod a naucit se ho, er diagram, doplnit databazi,
#TODO, kouknout na projekt podle zadani,, typy eventů, location, minulé eventy, procházející, budoucí
#  uživatele doplnit, možná i nějakou jinou domovskou stránku udělat a pak mít events v liště, možná celá republika zpátky
#  zeptat se Petra, jestli nám projde ty teplates, jestli je to v pořádku.

#TODO   testy, odstranit když je člověk odhlášeny okénko ADD COMMENT , ošetřit aby nešlo udělat stejné akce, aby akce nemohla končit dřív než začíná atd.
#TODO aby ve filtru zůstalo to, co tam člověk zadal, createevent pouze uživatel se speciální rolí,
#TODO testování webových stránek
