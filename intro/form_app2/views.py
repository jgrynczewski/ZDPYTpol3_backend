import os

from django.shortcuts import render

FILENAME = "tasks.txt"
is_file_exists = os.path.isfile(FILENAME)

if not is_file_exists:
    with open('tasks.txt', 'w+') as f:
        pass

# Create your views here.
def index(request):
    task = request.GET.get('task')

    if task:
        with open(FILENAME, 'a+') as f:
            f.write(f"{task}\n")

    with open(FILENAME, 'r') as f:
        tasks = f.readlines()

    return render(request, 'form_app2/index.html', {'tasks': tasks})


def register(request):
    return render(request, 'form_app2/register.html')
