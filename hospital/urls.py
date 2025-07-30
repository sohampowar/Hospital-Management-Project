from django.urls import path
from . import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login_', views.login_,name='login_'),
    path('add_patient',views.add_patient,name='add_patient'),
    path('profile',views.profile,name='profile'),
    path('patient_list',views.patient_list,name='patient_list'),
    path('edit_patient',views.edit_patient,name='edit_patient'),
    path('logout_',views.logout_,name='logout_'),
    path('up_profile',views.up_profile,name='up_profile'),
    path('change_pw',views.change_pw,name='change_pw'),
]