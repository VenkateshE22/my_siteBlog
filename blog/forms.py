
from django import forms


from blog.models import Post

class UploadDataForm(forms.ModelForm):
    
    
    class Meta:
        model = Post
        fields='__all__'
        exclude=['author']

