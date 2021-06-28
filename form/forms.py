from django import forms
from . models import UserInfo
 
class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('userName', 'country','sex','address')
        labels={
           'userName':'名前',
           'country':'出身国',
           'sex':'性別',
           'address':'住所',
           }