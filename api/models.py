from django.db import models
from django.contrib.auth.models import User
# Create your models here.


EVENT_TYPE_CHOICES = [
    (1, '时间'),
    (2, '频率'),
    (3, '计量')
]


class Event(models.Model):
    """event"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    datetime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    type = models.IntegerField(choices=EVENT_TYPE_CHOICES)
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=100)

    time = models.TimeField(null=True, blank=True)

    frequency = models.IntegerField(null=True, blank=True)

    amount = models.FloatField(null=True, blank=True)


class EventLog(models.Model):
    """clock event 记录"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.CharField(max_length=100, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(null=True, blank=True)

