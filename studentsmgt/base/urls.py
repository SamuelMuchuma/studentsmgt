from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *
from . import views
from rest_framework import routers

# Router for ModelViewSet


router = routers.SimpleRouter()

router.register(r'activities', views.ActivitiyModelViewSet, basename="activity")
router.register(r'students', views.StudentsModelViewSet, basename="student")
urlpatterns =[
    # Token Auth paths
    path('login/', obtain_auth_token, name="obtain_auth_token"),
    path('register/', RegisterAPI.as_view(), name='register'),

    # App URLs
    path('student/', views.StudentListAPIView.as_view(), name="students"),
    path('list-activities/', views.ActivityListAPIView.as_view(), name="activities"),

] + router.urls # Concatenating router urls
