from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForm, LoginForm


# Home
def home(request):
    # Here we not need to write the template/webapp/index.html because django by default knows what template is.
    return render(request, 'webapp/index.html')

# Register
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)

def login(request):
    return HttpResponse("<h1>Welcome to Django Project: Contact page</h1>")