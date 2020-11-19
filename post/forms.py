from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    picture = forms.ImageField(required = True)
    caption = forms.CharField(widget = forms.Textarea(attrs={'class':'input is-medium'}), required=True)
    tags = forms.CharField(widget = forms.TextInput(attrs={'class':'input is-medium','placeholder':'Seperate each tags by semi-colon ie.;'}), required=True)

    class Meta:
        model = Post
        fields = ('picture','caption','tags')
        