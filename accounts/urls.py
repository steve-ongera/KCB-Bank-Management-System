from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name="signup"),  # Registration page
    path("login/", views.sign_in, name="signin"),      # Login page
    path("logout/", views.logout_view, name="logout"),  # Logout page
]
