from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user": 'Username',
            "email": 'Email',
            "text": "Comment",
        }