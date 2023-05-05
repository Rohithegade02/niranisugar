from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('manager', views.manager, name='manager'),
    path('emp', views.emp, name='emp'),
    path('home', views.home, name='home'),
    path('addleaveapp', views.addleaveapp, name='addleaveapp'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('shifts', views.viewempshift, name='view-shift'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout, name='logout'),
    path('applications', views.viewapp, name='leave-applications'),
    path('employees', views.viewemp, name='view-employees'),
    path('addempshift', views.addempshift, name='add-employees-shift'),
    path('shiftpolicy', views.shiftpolicy, name='shift-policy'),
    path('applications/<int:model_id>/update_true/', views.update_true_model, name='update_true_model'),
    path('applications/<int:model_id>/update_false/', views.update_false_model, name='update_false_model'),
]