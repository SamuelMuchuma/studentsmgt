from django.shortcuts import render
from knox.models import AuthToken
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import filters, generics
from .serializers import *

from .models import *


# Create your views here.

# Register user
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# students list readonly endpoint using generic views -ListAPYView
class StudentListAPIView(ListAPIView):
    # the user has to be authenticated to view this view
    permission_classes = (IsAuthenticated,)

    queryset = Students.objects.all()
    serializer_class = ReadStudentsSerializer


# School activities list read-only endpoint using ListAPIViews
class ActivityListAPIView(ListAPIView):
    # the user has to be authenticated to view this view
    permission_classes = (IsAuthenticated,)

    queryset = School_Activities.objects.all()
    serializer_class = ActivitySerializer


# School activities endpoint using ModelViewSet
class ActivitiyModelViewSet(ModelViewSet):
    # the user has to be authenticated to view this view
    permission_classes = (IsAuthenticated,)

    # Set this view to a global view. Any auth user can CRUD school activies. Students belong to specific auth teachers
    queryset = School_Activities.objects.all()
    serializer_class = ActivitySerializer


# Students endpoint using ModelViewSet
class StudentsModelViewSet(ModelViewSet):
    # the user has to be authenticated to view this view
    permission_classes = (IsAuthenticated,)

    # Search filter
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ("student_ID",)
    # Order search results by. N/A since search returns one item in this case
    ordering_fields = ("student_ID")

    # specify related fields to improve performance .select_related("field1", "field2")
    def get_queryset(self):
        return Students.objects.select_related("activity", "user").filter(user=self.request.user)

    # specify serializer depending on the request
    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadStudentsSerializer
        return WriteStudentsSerializer
