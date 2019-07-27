import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.utils import timezone

from rest_framework import viewsets, permissions, mixins, serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import EventSerializer, EventLogSerializer
from .models import Event, EventLog

@ensure_csrf_cookie
def index(request):
    print(request.session)
    print(request.user)
    return render(request, 'index.html')


def signup(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    first_name = request.POST.get('username')

    if not username:
        return JsonResponse({'msg': 'Invalid Username'}, status=400)
    if not password:
        return JsonResponse({'msg': 'Invalid password'}, status=400)
    if not email:
        return JsonResponse({'msg': 'Invalid email'}, status=400)
    try:
        User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name='',
            email=email,
            is_staff=False,
            is_active=True
        )
        return JsonResponse({'msg': 'Success'})
    except Exception as e:
        print(e)
        return JsonResponse({'msg': 'Fail'}, status=400)


def login_(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if not username:
        return JsonResponse({'msg': 'Invalid Username'}, status=400)
    if not password:
        return JsonResponse({'msg': 'Invalid password'}, status=400)

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

    else:
        return JsonResponse({'msg': 'Invalid User'}, status=400)
    return JsonResponse({'msg': 'Login Success'})


def logout_(request):
    logout(request)
    return HttpResponse('ok')


def check_session(request):
    if request.user.is_authenticated:
        return JsonResponse({'username': request.user.username})
    return JsonResponse({'info': '无效session'}, status=404)


@login_required()
def test(request):
    print(request.user)
    print(dir(request))
    return HttpResponse('ok')


class EventViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Event.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        1.  request.data和 serializer data 不一致时 需改写view函数，按需求修改request.data后传入serializer
        2.  在serializer.py中 validate_****** 校验并返回值，只能处理key一样的数据
        3.  perform_create函数是在保存到数据库之前修改校验以后的数据
        4.  Nested relationships的情况下需要改写serializer的create函数  *By default nested serializers are read-only.*
        """
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class EventLogViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    serializer_class = EventLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return EventLog.objects.filter(user=user)

    def perform_create(self, serializer):
        event = Event.objects.get(id=self.request.data['event_id'])
        serializer.save(user=self.request.user, event=event)

    def create(self, request, *args, **kwargs):
        """
        1.  request.data和 serializer data 不一致时 需改写view函数，按需求修改request.data后传入serializer
        2.  在serializer.py中 validate_****** 校验并返回值，只能处理key一样的数据
        3.  perform_create函数是在保存到数据库之前修改校验以后的数据
        4.  Nested relationships的情况下需要改写serializer的create函数  *By default nested serializers are read-only.*
        """
        today_min = datetime.datetime.combine(timezone.now().today(), datetime.time.min)
        today_max = datetime.datetime.combine(timezone.now().today(), datetime.time.max)
        is_log = EventLog.objects.filter(datetime__range=(today_min, today_max), event_id=request.data['event_id']).exists()
        if is_log:
            return Response('今日已经记录', status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
