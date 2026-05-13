from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass", team=self.team)
        self.workout = Workout.objects.create(name="Cardio", description="Cardio workout", duration=30)
        self.activity = Activity.objects.create(user=self.user, type="run", duration=30, calories=200)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), "Test Team")

    def test_user_email(self):
        self.assertEqual(self.user.email, "test@example.com")

    def test_activity_type(self):
        self.assertEqual(self.activity.type, "run")

    def test_workout_name(self):
        self.assertEqual(self.workout.name, "Cardio")

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 100)
