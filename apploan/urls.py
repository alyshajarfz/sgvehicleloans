from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('', views.home, name='home'),
    path('financeUsed/', views.financeUsed, name='financeUsed'),
    path('financeDirect/', views.financeDirect, name='financeDirect'),
    path('financeNew/', views.financeNew, name='financeNew'),
    path('financeCOECar/', views.financeCOECar, name='financeCOECar'),
    path('financeRefinance/', views.financeRefinance, name='financeRefinance'),
    path('financeInHouse/', views.financeInHouse, name='financeInHouse'),
    path('financePHVCar/', views.financePHVCar, name='financePHVCar'),

    path('COERenewCar/', views.COERenewCar, name='COERenewCar'),
    path('COERenewMoto/', views.COERenewMoto, name='COERenewMoto'),

    path('insMotor/', views.insMotor, name='insMotor'),
    path('insCar/', views.insCar, name='insCar'),

    path('rates/', views.rates, name='rates'),

    path('guidesCalc/', views.guidesCalc, name='guidesCalc'),
    path('guidesFaq/', views.guidesFaq, name='guidesFaq'),
    path('guidesInstall/', views.guidesInstall, name='guidesInstall'),
    path('guidesPay/', views.guidesPay, name='guidesPay'),

    path('about/', views.about, name='about'),

    path('contact/', views.contact, name='contact'),

    path('apply/', views.apply, name='apply'),
    path('enquire/', views.enquire, name='enquire'),
    path('mQuote/', views.mQuote, name='mQuote'),
    path('cQuote/', views.cQuote, name='cQuote'),
    
    path('formCar/', views.formCar, name='formCar'),
    path('formMotor/', views.formMotor, name='formMotor'),

]
