from django.urls import path
from . import views

urlpatterns = [
    # Add .as_view() in order to django find get and post methods
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view(), name="reviews-list"),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view(), name="review-detail")
]
