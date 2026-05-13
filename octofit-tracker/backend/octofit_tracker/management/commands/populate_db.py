from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Borrar datos existentes en orden correcto para evitar problemas de claves foráneas
        for model in [Leaderboard, Activity, Workout, User, Team]:
            try:
                model.objects.all().delete()
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"No se pudo borrar datos de {model.__name__}: {e}"))

        # Crear equipos
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Crear usuarios
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel)
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc)
        superman = User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc)

        # Crear actividades
        Activity.objects.create(user=ironman, type='Running', duration=30, calories=300)
        Activity.objects.create(user=spiderman, type='Cycling', duration=45, calories=400)
        Activity.objects.create(user=batman, type='Swimming', duration=60, calories=500)
        Activity.objects.create(user=superman, type='Yoga', duration=40, calories=200)

        # Crear workouts
        Workout.objects.create(name='Full Body', description='Entrenamiento completo', duration=60)
        Workout.objects.create(name='Cardio', description='Entrenamiento cardiovascular', duration=45)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, points=1000)
        Leaderboard.objects.create(user=spiderman, points=900)
        Leaderboard.objects.create(user=batman, points=950)
        Leaderboard.objects.create(user=superman, points=1100)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
