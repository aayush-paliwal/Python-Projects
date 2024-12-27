from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=''),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('record/<int:rId>', views.single_record, name='record'),
    path('create-record', views.create_record, name='create-record'),
    path('update-record/<int:rId>', views.update_record, name='update-record'),
    path('delete-record/<int:rId>', views.delete_record, name='delete-record'),
]