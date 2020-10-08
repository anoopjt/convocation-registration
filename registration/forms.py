from django import forms
from captcha.fields import CaptchaField
from registration import models

class DateInput(forms.DateInput):
    input_type = 'date'

class StudentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Student
        widgets = {'transaction_date': DateInput()}
        exclude = ['id']
