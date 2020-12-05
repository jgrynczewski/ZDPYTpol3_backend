from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from form_app3.models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()

    task = request.GET.get('task')
    if task:
        Task.objects.create(text=task)

    return render(request, 'form_app3/index.html', {"tasks": tasks})


def register(request):
    return render(request, 'form_app3/register.html')


@require_http_methods(["GET", "POST"])
def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    updated_task_text = request.POST.get('task')
    if updated_task_text:
        task.text = updated_task_text
        task.save()

        return redirect("form3:index")

    return render(request, "form_app3/update.html", {"task": task})


@require_http_methods(["POST"])
def delete(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()

    return redirect("form3:index")
