from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.


class ReviewView(CreateView):
    model = Review
    # You can use all fields from Review MODEL to CREATE a FormView
    # Add fields as in forms.py __all__ if you want to add all
    # fields = '__all__'
    
    # If you want to configure more than fields (Like labels, error messages)
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"
    
    #It will redirect to success url, validate and save data in database
    #so we don't need form_valid() function as in FormView.
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Check all reviews: '
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt=5)
        return data


class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review
