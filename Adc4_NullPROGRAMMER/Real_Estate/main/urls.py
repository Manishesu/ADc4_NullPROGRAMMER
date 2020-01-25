
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/',views.register_user, name="signup"),
    path('login/',views.authenticate_user, name="login"),

]
