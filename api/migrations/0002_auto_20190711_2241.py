# Generated by Django 2.2.3 on 2019-07-11 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('type', models.IntegerField(choices=[(1, '时间'), (2, '频率'), (3, '计量')])),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=100)),
                ('time', models.TimeField(blank=True, null=True)),
                ('frequency', models.IntegerField(blank=True, null=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='EventLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='clockeventlog',
            name='event',
        ),
        migrations.RemoveField(
            model_name='clockeventlog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='frequencyevent',
            name='user',
        ),
        migrations.RemoveField(
            model_name='frequencyeventlog',
            name='event',
        ),
        migrations.RemoveField(
            model_name='frequencyeventlog',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClockEvent',
        ),
        migrations.DeleteModel(
            name='ClockEventLog',
        ),
        migrations.DeleteModel(
            name='FrequencyEvent',
        ),
        migrations.DeleteModel(
            name='FrequencyEventLog',
        ),
    ]
