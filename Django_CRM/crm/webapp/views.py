from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # Here we not need to write the template/webapp/index.html because django by default knows what template is.
    return render(request, 'webapp/index.html')

def about(request):
    return HttpResponse("<h1>Welcome to Django Project: About page</h1>")

def contact(request):
    return HttpResponse("<h1>Welcome to Django Project: Contact page</h1>")