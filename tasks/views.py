from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import CreateTaskModelForm
from tasks.models import Task


def index(request):
    if request.method == "POST":
        form = CreateTaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CreateTaskModelForm()

    context = {
        "tasks": Task.objects.all(),
        "form": form,
    }

    return render(request, "home.html", context)


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.filter(username=username).first()

        if user:

            return HttpResponse("Já existe um usuário com esse nome")

        user = User.objects.create_user(username=username, password=password)
        user.save()

        return redirect("/login/")


def user_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            return redirect("/tasks/")
        else:
            return HttpResponse("Usuário ou senha inválidos")


def user_logout(request):
    logout(request)
    return redirect("/")


@login_required(login_url="/login/")
def tasks_list(request):
    status_filter = request.GET.get("status")

    if status_filter == "completed":
        tasks = Task.objects.filter(user=request.user, completed=True)
    elif status_filter == "pending":
        tasks = Task.objects.filter(user=request.user, completed=False)
    else:
        tasks = Task.objects.filter(user=request.user)

    context = {"tasks": tasks}

    return render(request, "tasks_list.html", context)


@login_required(login_url="/login/")
def create_task(request):
    if request.method == "POST":
        form = CreateTaskModelForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("/tasks/")
    else:
        form = CreateTaskModelForm()

    context = {
        "form": form,
    }

    return render(request, "create_task.html", context)


@login_required(login_url="/login/")
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        form = CreateTaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/tasks/")
    else:
        form = CreateTaskModelForm(instance=task)

    context = {
        "form": form,
        "task": task,
    }

    return render(request, "edit_task.html", context)


@login_required(login_url="/login/")
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect(request.META.get("HTTP_REFERER"))

    context = {
        "task": task,
    }

    return render(request, "delete_task.html", context)


@login_required(login_url="/login/")
def toggle_task_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect(request.META.get("HTTP_REFERER"))
