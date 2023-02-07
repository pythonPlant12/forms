from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        # Add all fields from Model using '__all__'
        fields = '__all__'
        # Exclude any field
        # exclude = ['']
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty!",
                "max_length": "The lenght should not be more than 100!"
            }
        }
