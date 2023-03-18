from http import HTTPStatus

from django.shortcuts import render


def csrf_failure(request, reason=''):
    return render(request, 'core/403csrf.html', status=HTTPStatus.FORBIDDEN)


def page_not_found(request, exception):
    return render(request, 'core/404.html', status=HTTPStatus.NOT_FOUND)


def internal_server_error(request):
    return render(request, 'core/500.html', status=HTTPStatus.INTERNAL_SERVER_ERROR)
