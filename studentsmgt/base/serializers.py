from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['email'], validated_data['password'])

        return user


# Serializer for the user model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
        )
        read_only_fields = fields


# Activity model serializer
class ActivitySerializer(serializers.ModelSerializer):
    # Set the default user value and hide
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = School_Activities
        fields = "__all__"


# students model serializer
class WriteStudentsSerializer(serializers.ModelSerializer):
    # Set the default user value and hide
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # Display activity name instead of ID
    activity = serializers.SlugRelatedField(slug_field="name", queryset=School_Activities.objects.all())

    class Meta:
        model = Students
        fields = "__all__"


# This class returns nested objects of the related fields
class ReadStudentsSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # Display activity name instead of ID
    activity = ActivitySerializer()

    class Meta:
        model = Students
        fields = (
            "id",
            "student_ID",
            "first_name",
            "second_name",
            "activity",
            # "user",

        )
        read_only_fields = fields
