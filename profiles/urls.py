from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("user-profile", views.ProfilesView.as_view()),
]