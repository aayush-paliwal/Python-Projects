from django.shortcuts import render, redirect

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from .models import Record


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


            return redirect("login")

    context = {'form':form}

    return render(request, 'webapp/register.html', context=context)


# Login user
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")
    
    context = {'form': form}

    return render(request, 'webapp/login.html', context=context)


# Logout user
def logout(request):

    auth.logout(request)


    return redirect("login")


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)


# Create a new record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()

    if request.method == 'POST':
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)


# Update record
@login_required(login_url='login')
def update_record(request, rId):
    record = Record.objects.get(id=rId)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            return redirect('dashboard')
    
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context) 



#  Read/View single record
@login_required(login_url='login')
def single_record(request, rId):
    all_records = Record.objects.get(id=rId)

    context = {'record': all_records}
    return render(request, 'webapp/view-record.html', context=context)


# Delete a record
@login_required(login_url='login')
def delete_record(request, rId):
    record = Record.objects.get(id=rId)

    record.delete()
    return redirect('dashboard')