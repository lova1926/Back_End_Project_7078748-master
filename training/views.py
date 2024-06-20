from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm

@login_required
def start_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('update_workout', workout_id=workout.id)
    else:
        form = WorkoutForm()
    return render(request, 'training/start_workout.html', {'form': form})

@login_required
def update_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.workout = workout
            exercise.save()
            return redirect('update_workout', workout_id=workout.id)
    else:
        form = ExerciseForm()
    exercises = workout.exercises.all()
    return render(request, 'training/update_workout.html', {'workout': workout, 'form': form, 'exercises': exercises})

@login_required
def stop_workout(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    workout.end_time = timezone.now()
    workout.save()
    return redirect('user_profile')

@login_required
def workout_detail(request, workout_id):
    workout = get_object_or_404(Workout, id=workout_id, user=request.user)
    exercises = workout.exercises.all()
    return render(request, 'training/workout_detail.html', {'workout': workout, 'exercises': exercises})
