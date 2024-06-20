from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Goal
from .forms import GoalForm

@login_required
def create_goal(request):
    if request.method == 'POST':
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect('user_profile')
    else:
        form = GoalForm()
    return render(request, 'goals/create_goal.html', {'form': form})

@login_required
def goal_detail(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == 'POST':
        goal.completed = not goal.completed
        goal.save()
        return redirect('user_profile')
    return render(request, 'goals/goal_detail.html', {'goal': goal})
