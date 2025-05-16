from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods, require_POST
from django.db.models import Q
from datetime import date

from .forms import RegisterForm, TodoForm, TaskListForm
from .models import Todo, TaskList

# -------------------------------
# AUTH
# -------------------------------

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('login')

# -------------------------------
# TODO LIST
# -------------------------------

@login_required
def todo_list(request):
    list_id = request.GET.get('list')

    task_lists = TaskList.objects.filter(
        Q(user=request.user) | Q(shared_with=request.user)
    ).distinct()

    if list_id:
        todos = Todo.objects.filter(
            Q(list_id=list_id),
            Q(list__user=request.user) | Q(list__shared_with=request.user)
        ).distinct()
    else:
        todos = Todo.objects.filter(
            Q(list__user=request.user) | Q(list__shared_with=request.user)
        ).distinct()

    today = date.today()
    return render(request, 'todo/todo_list.html', {
        'todos': todos,
        'today': today,
        'task_lists': task_lists,
        'active_list_id': int(list_id) if list_id else None,
    })

@login_required
def add_todo(request):
    list_id = request.GET.get('list')
    if request.method == 'POST':
        form = TodoForm(request.POST, user=request.user)
        if form.is_valid():
            todo = form.save(commit=False)
            task_list = todo.list
            if task_list.user == request.user or request.user in task_list.shared_with.all():
                todo.user = request.user
                todo.save()
                return redirect(f"/?list={task_list.id}")
    else:
        form = TodoForm(user=request.user)
    return render(request, 'todo/add_todo.html', {'form': form})

@login_required
def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    list_id = todo.list.id
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo, user=request.user)
        if form.is_valid():
            form.save()
            return redirect(f"/?list={list_id}")
    else:
        form = TodoForm(instance=todo, user=request.user)
    return render(request, 'todo/edit_todo.html', {'form': form})

@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    list_id = todo.list.id
    todo.delete()
    return redirect(f"/?list={list_id}")

@require_POST
@login_required
def toggle_completed(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    # ➤ Samo autor zadatka može označiti kao dovršen
    if todo.user != request.user:
        return JsonResponse({
            'status': 'forbidden',
            'message': 'Samo autor zadatka može označiti izvršenost.'
        }, status=403)

    todo.completed = not todo.completed
    todo.save()

    list_id = request.GET.get('list')
    if list_id:
        return redirect(f"/?list={list_id}")
    return redirect('todo_list')


# -------------------------------
# TASK LIST (KATEGORIJE)
# -------------------------------

@login_required
def add_list(request):
    if request.method == 'POST':
        form = TaskListForm(request.POST, user=request.user)
        if form.is_valid():
            task_list = form.save(commit=False)
            task_list.user = request.user
            task_list.save()
            form.instance = task_list
            form.save_m2m()
            return redirect('todo_list')
    else:
        form = TaskListForm(user=request.user)
    return render(request, 'todo/add_list.html', {'form': form})

@login_required
def edit_list(request, pk):
    task_list = get_object_or_404(TaskList, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskListForm(request.POST, instance=task_list, user=request.user)
        if form.is_valid():
            form.save()
        return redirect(f"/?list={task_list.id}")
    else:
        return redirect('todo_list')

@require_http_methods(["POST"])
@csrf_protect
@login_required
def delete_list(request, list_id):
    task_list = get_object_or_404(TaskList, id=list_id)

    if task_list.user != request.user:
        return JsonResponse({
            'status': 'forbidden',
            'message': 'Ne možeš obrisati ovu listu jer nisi njezin vlasnik.'
        }, status=403)

    task_list.delete()
    return JsonResponse({'status': 'ok'})
