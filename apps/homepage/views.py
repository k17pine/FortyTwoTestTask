from django.http import HttpResponse
from django.shortcuts import render, redirect

def hello(request):
    #return HttpResponse("Hello.")
    return render(request=request, template_name="homepage/index.html")