from django.db import models
from django.utils import timezone
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Title(models.Model):
    STATUS_CHOICES = (
        ('TOWATCH','To Watch'),
        ('WATCHING','Watching'),
        ('WATCHED','Watched'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, blank=True, on_delete=models.CASCADE,)
    title = models.CharField(max_length=120)
    japanese_title = models.CharField(max_length=120)
    created_at = models.DateField(default=timezone.now,blank=True)

    year = models.IntegerField(default=2018, validators=[
            MaxValueValidator(2022),
            MinValueValidator(1960)
        ])

    rating = models.IntegerField(default=0, validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ])
    review = models.TextField(blank=True)

    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='TOWATCH')

    def __str__(self):
        return self.title
