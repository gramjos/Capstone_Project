from django.forms import ModelForm, Textarea
#from socket import fromshare
from .models import Review, Comment
from django import forms


class ReviewForm(ModelForm):

    def __init__(self, *args, **kwargs):

        super(ModelForm, self).__init__(*args,**kwargs)

        self.fields['text'].widget.attrs.update({'class': 'form-control'})

        self.fields['watchAgain'].widget.attrs.update({'class': 'form-check-input'})

    class Meta:

        model = Review

        fields = ['text','watchAgain']    

        labels = {'watchAgain': ('Watch Again') }

        widgets = {'text': Textarea(attrs={'rows': 4}),}

        

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        #fields = "__all__"
        fields = ['city', 'content', 'user']
        widgets = {
            'user': forms.TextInput(attrs={'type':'hidden'}),
            'content': forms.Textarea()

            }