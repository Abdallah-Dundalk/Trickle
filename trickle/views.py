from django.shortcuts import render


def page_not_found(request, exception):
    return rednder(request, '404.html', status=404)
