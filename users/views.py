from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib import messages
from .forms import UserRegisterForm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from goals.models import Goal
from training.models import Workout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form = UserProfileForm(instance=request.user.userprofile)
    
    goals = Goal.objects.filter(user=request.user)
    workouts = Workout.objects.filter(user=request.user)
    completed_goals = goals.filter(completed=True).count()
    total_goals = goals.count()
    if total_goals > 0:
        completion_rate = (completed_goals / total_goals) * 100
    else:
        completion_rate = 0
    
    # Generare il grafico
    fig, ax = plt.subplots(figsize=(6, 2))
    ax.axhline(1, xmin=0, xmax=completion_rate/100, color=get_color(completion_rate), linewidth=10)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 2)
    ax.set_yticks([])
    ax.set_title('Goal Completion Rate')
    ax.set_xlabel('Completion Percentage')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = 'data:image/png;base64,' + string.decode('utf-8')
    plt.close(fig)
    
    return render(request, 'users/user_profile.html', {
            'form': form, 
            'goals': goals, 
            'workouts': workouts,  
            'chart': uri,
            'username': request.user.username, 
        })

def get_color(rate):
    if rate <= 30:
        return 'red'
    elif rate <= 70:
        return 'orange'
    else:
        return 'green'










