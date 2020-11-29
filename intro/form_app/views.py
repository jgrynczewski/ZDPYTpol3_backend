from django.shortcuts import render

TASKS = []


# Create your views here.
def index(request):
    task = request.GET.get('task')
    if task:
        TASKS.append(task)

    return render(request, 'form_app/index.html', {"tasks": TASKS})


def register(request):
    return render(request, 'form_app/register.html')