from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListApiView.as_view()),
    path('<int:pk>/', views.CourseDetailUpdateDeleteApiView.as_view()),
]