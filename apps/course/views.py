from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter
from rest_framework import serializers

from .models import CourseModel
from .serializers import CourseSerializer
from .permissions import IsAdminOrReadOnly


class CourseListApiView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly)
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer

    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('name', 'description', 'start_date', )


class CourseDetailUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated, IsAdminOrReadOnly )
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer