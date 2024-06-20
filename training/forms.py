from django import forms
from .models import Workout, Exercise

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['title']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'sets', 'reps', 'weight']
