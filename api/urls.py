from django.urls import path
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'event',  views.EventViewSet, base_name='event')
router.register(r'log',  views.EventLogViewSet, base_name='eventlog')

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_, name='login'),
    path('logout/', views.logout_, name='logout'),
    path('test/', views.test, name='test'),
    path('check_session/', views.check_session, name='check_session'),
]

urlpatterns += router.urls
