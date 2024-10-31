from django.db import models

from datetime import datetime

from django.core.validators import MinValueValidator
from django.db.models import ForeignKey
from django.urls import reverse


class Coords(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name='Широта', blank=True, null=True)
    longitude = models.FloatField(max_length=50, verbose_name='Долгота', blank=True, null=True)
    height = models.IntegerField(verbose_name='Высота', blank=True, null=True)


    def __str__(self):
        return f'{self.latitude} {self.longitude} {self.height}'


class Level(models.Model):
    level_1A = '1A'
    level_1B = '1B'
    level_2A = '1A'
    level_2B = '2B'
    level_3A = '3A'
    level_3B = '3B'

    LEVEL_CHOICES = (
        (level_1A, '1A'),
        (level_1B, '1Б'),
        (level_2A, '2A'),
        (level_2B, '2Б'),
        (level_3A, '3A'),
        (level_3B, '3Б'),
    )

    winter = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    spring = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    summer = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    autumn = models.CharField(max_length=2, choices=LEVEL_CHOICES)


    def __str__(self):
        return f'{self.winter} {self.spring} {self.summer} {self.autumn}'


class PassUser(models.Model):
    email = models.EmailField(max_length=64)
    fam = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    otc = models.CharField(max_length=120)
    phone = models.CharField(max_length=64)


    def __str__(self):
        return f'{self.email} {self.fam} {self.name} {self.otc} {self.phone}'


class Pereval(models.Model):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'

    STATUS = [
        (new, "новый"),
        (pending, "модератор взял в работу"),
        (accepted, "модерация прошла успешно"),
        (rejected, "модерация прошла, информация не принята"),
    ]

    beauty_title = models.CharField(max_length=255, verbose_name='Название препятствия')
    title = models.CharField(max_length=255, verbose_name='Название вершины')
    other_titles = models.CharField(max_length=255, verbose_name='Другое название')
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(PassUser, on_delete=models.CASCADE, related_name='user')
    coords = ForeignKey(Coords, on_delete=models.CASCADE)
    level = ForeignKey(Level, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS, default=new)
    connect = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'{self.pk} {self.beauty_title}'


class Images(models.Model):
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, blank=True, null=True,
                                related_name='images')
    data = models.URLField(verbose_name='Изображение', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Название', blank=True, null=True)
    date_added = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.pk} {self.title}'