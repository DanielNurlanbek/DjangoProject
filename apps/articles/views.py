from django.shortcuts import render

from django.http import HttpResponse


def article_1(request):
    return HttpResponse("Статья 1!")


def article_2(request):
    html = ("<html>"
            "<body>"
            "<h1>"
            "Статья 2!"
            "</h1>"
            "</body>"
            "</html>")
    return HttpResponse(html, status=200)
