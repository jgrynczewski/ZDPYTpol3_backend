from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def cookie(request):
    # print(dir(request))
    print(request.COOKIES)
    response = HttpResponse("OK")

    response.set_cookie("ciasteczko1", 5)
    response.set_cookie("ciasteczko2", 10, max_age=1000)

    return response


def session(request):
    # print(dir(request))
    # print(dir(request.session))
    # print(request.session.session_key)
    # key = request.session._get_or_create_session_key()

    num_visit = request.session.get("num_visit", 0) + 1
    request.session['num_visit'] = num_visit
    return HttpResponse(f"Liczba odwiedzin: {num_visit}")
