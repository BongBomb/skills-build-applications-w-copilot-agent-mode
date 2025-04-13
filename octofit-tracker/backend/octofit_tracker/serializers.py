from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    members = serializers.ListField()

class ActivitySerializer(serializers.Serializer):
    user = UserSerializer()
    type = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    team = TeamSerializer()
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    user = UserSerializer()
    description = serializers.CharField()
    date = serializers.DateField()
