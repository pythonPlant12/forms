from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile
# Create your views here.


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })

    def post(self, request):
        submitted_file = ProfileForm(request.POST, request.FILES)
        if submitted_file.is_valid():
            # Now name of request.FILES will be the name of a method in FormClass
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")
        else:
            return render(request, "profiles/create_profile.html", {
                "form": submitted_file
            })
