from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from tasks.forms import CreateTaskModelForm


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


def tasks_list(request):
    status_filter = request.GET.get("status")

    if status_filter == "completed":
        tasks = Task.objects.filter(completed=True)
    elif status_filter == "pending":
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()

    context = {"tasks": tasks}

    return render(request, "tasks_list.html", context)


def create_task(request):
    if request.method == "POST":
        form = CreateTaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/tasks/")
    else:
        form = CreateTaskModelForm()

    context = {
        "form": form,
    }

    return render(request, "create_task.html", context)


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


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return redirect(request.META.get("HTTP_REFERER"))

    context = {
        "task": task,
    }

    return render(request, "delete_task.html", context)


def toggle_task_completion(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect(request.META.get("HTTP_REFERER"))
