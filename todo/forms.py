
from  django import forms
class task_form(forms.Form):
    id=forms.CharField()
    name=forms.CharField()
    is_done=forms.ChoiceField(choices=[('true','True'),('false','False')])
    description=forms.CharField(widget=forms.Textarea)
