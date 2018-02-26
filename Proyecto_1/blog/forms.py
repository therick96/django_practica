from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields["title"].widget.attrs = {
            'class' : 'uk-input',
        }
        self.fields["text"].widget.attrs = {
            'class' : "uk-textarea",
            'rows' : 20,
        }
        
    class Meta:
        model = Post
        fields = ["title", "text"]
