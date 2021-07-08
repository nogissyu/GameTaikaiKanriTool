from django import forms
from . models import UserInfo, battledata, Entry
 
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

class dataForm(forms.ModelForm):
    class Meta:
        model = battledata
        fields = ('battleID','userID1','userID2','winner')
        labels={
           'battleID':'1',
           'userID1':'出身国',
           'userID2':'性別',
           'winner':'0',
           }

class PlaierForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('userID', 'username')
        labels={
           'userID':'ID',
           'username':'名前',
           }