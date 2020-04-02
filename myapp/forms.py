from django import forms
from myapp.models import MyModel

from .models import Files
#DataFlair #File_Upload
class File(forms.ModelForm):
    class Meta:

        model = Files
        fields = '__all__'
        

class MyModel(forms.ModelForm):
    

    class Meta:
        model = MyModel
        fields="__all__"
        widgets = {'Symptoms': forms.CheckboxSelectMultiple}
