from django.contrib import admin
from django.urls import path, include

from leetcodeapp import views

urlpatterns = [
    path('signup',views.signup),
    path('problems',views.problems,name='problems'),
    path('',views.home),
    path('login',views.login, name='login')
]
