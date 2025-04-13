from rest_framework.views import APIView
from rest_framework.response import Response

class UserList(APIView):
    def get(self, request):
        return Response({'message': 'List of users'})

class TeamList(APIView):
    def get(self, request):
        return Response({'message': 'List of teams'})

class ActivityList(APIView):
    def get(self, request):
        return Response({'message': 'List of activities'})

class LeaderboardList(APIView):
    def get(self, request):
        return Response({'message': 'Leaderboard'})

class WorkoutList(APIView):
    def get(self, request):
        return Response({'message': 'List of workouts'})

def api_root(request):
    return Response({'message': 'API Root'})
