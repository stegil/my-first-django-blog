from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = ost
        fields = (
            "title",
            "text",
        )
