from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        fields = ('comment_content', )
        widgets = {
            'comment_content': forms.Textarea(attrs={'class': 'form-control', 'cols': 150, 'rows': 10}),
        }
