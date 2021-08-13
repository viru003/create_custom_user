from django.urls import path, include
from .views import *

urlpatterns = [
    path('', LoginView.as_view(), name="index"),
    path('register',RegisterView.as_view(), name="register"),
    path('dashboard',dashboard,name="dashboard"),
    path('logout_view',logout_view,name="logout_view")

]