from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import CourseModel

User = get_user_model()

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseModel
        fields = ('__all__')
