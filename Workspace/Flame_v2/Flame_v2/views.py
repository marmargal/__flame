from django.shortcuts import render

def header(request):
    return render(request, "header.html")

def inicio(request):
    return render(request, "test.html")