from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        user1 = User.objects.create(email='john.doe@example.com', name='John Doe', age=27)
        user2 = User.objects.create(email='jane.smith@example.com', name='Jane Smith', age=30)

        # Create test teams
        team1 = Team.objects.create(name='Team Alpha', members=[user1.id, user2.id])

        # Create test activities
        Activity.objects.create(user=user1, type='Running', duration=30)
        Activity.objects.create(user=user2, type='Cycling', duration=45)

        # Create test leaderboard
        Leaderboard.objects.create(team=team1, score=100)

        # Create test workouts
        Workout.objects.create(user=user1, description='Morning Yoga', date='2025-04-13')
        Workout.objects.create(user=user2, description='Evening Run', date='2025-04-13')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
