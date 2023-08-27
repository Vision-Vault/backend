from django import forms
from .models import Comment,ChildComment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['class'] ='input'
        self.fields['body'].widget.attrs['placeholder'] ='Add comment'


class CommentForm2(forms.ModelForm):
    class Meta:
        model = ChildComment
        fields = ['body']

    def __init__(self, *args, **kwargs):
        super(CommentForm2, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs['class'] ='input'
        self.fields['body'].widget.attrs['placeholder'] ='Add comment'
