from . models import Info
from django import forms
from django.forms import fields,ModelForm


class XYZ_DateInput(forms.DateInput):
    input_type = "date"
    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        # kwargs["format"] = "%d-%m-%Y"
        super().__init__(**kwargs)



class InfoForm(ModelForm):

    class Meta:


        model = Info
        fields=['Full_Name','Phone_number','Email','Age','Blood_Group','Address','City','Pin_code','State','Last_donated']
        widgets = {
            'Last_donated':XYZ_DateInput(format=["%Y-%m-%d"],)
            }

