from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось, причем вместе с сообщением в телеграм!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
