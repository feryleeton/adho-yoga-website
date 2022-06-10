from django import forms

from blog.models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['message', ]
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment here...',
                'id': 'content',
                'cols': 30,
                'rows': 7,
            }),
        }