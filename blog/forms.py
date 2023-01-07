from django import forms

from .models import Comment, Reply


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'text')
        widgets =  {
            'name' : forms.TextInput(attrs={'placeholder': '名前', 'class': 'form-control'}),
            'text' : forms.Textarea(attrs={'placeholder': 'コメント入力', 'class': 'form-control'}),
        }
        labels = {
            'name': '※必須',
            'text': '※必須',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('name', 'text')
        widgets =  {
            'name' : forms.TextInput(attrs={'placeholder': '名前', 'class': 'form-control'}),
            'text' : forms.Textarea(attrs={'placeholder': '返信コメント入力', 'class': 'form-control'}),
        }
        labels = {
            'name': '※必須',
            'text': '※必須',
        }
