from django.http import HttpResponse


def greet(request):
    return HttpResponse('Hello World')


def bye(request):
    return HttpResponse('Good bye!')


def adult(request, age):
    if age >= 18:
        return HttpResponse('Your are of age')
    else:
        return HttpResponse('Your are underage')
