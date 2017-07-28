from django import forms
from .models import tobedone

class task_form( forms.ModelForm ):
    title= forms.CharField(max_length=200)
    #detail= forms.TextField(blank=True)
    deadline = forms.DateField()
    pub_date = forms.DateTimeField('date published')
    finish= forms.BooleanField(default=False)
    class Meta:
        model = tobedone
        fields = ['title', 'detail','deadline','finish']
