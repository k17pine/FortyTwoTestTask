from django.shortcuts import render


def hello(request):
    return render(request=request, template_name="homepage/index.html")
