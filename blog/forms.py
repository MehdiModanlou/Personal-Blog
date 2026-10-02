from django import forms

from .models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [  # noqa: RUF012
            "title",
            "slug",
            "body",
            "published",
            "categories"
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [  # noqa: RUF012
            "body"
        ]