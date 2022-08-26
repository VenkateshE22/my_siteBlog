
from django import forms


from blog.models import Post, Category

#choices1 = Category.objects.all().values_list('name')

#choice_list = []

#for item in choices1:
    #choice_list.append(item)

class UploadDataForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        #category = forms.Select(choices=choice_list, attrs={'class':'form-control'})
        exclude = ['author']

class UpdateDataForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"
        #category = forms.Select(choices=choice_list, attrs={'class':'form-control'})
        # exclude = ['author','']
        # widgets={
        #     "title":forms.TextInput(
        #         attrs:{""})
        # }

class catagoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields="__all__"


