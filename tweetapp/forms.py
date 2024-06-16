from django import forms
from .models import User, Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['id', 'usr_id', 'tw_date', 'tw_time', 'content']
        labels = {'id':'投稿ID', 'usr_id':'ユーザ名', 'tw_date':'投稿日付', 'tw_time':'投稿時刻', 'content':'内容'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['id', 'name', 'age']
        labels = {'id':'ユーザID', 'name':'名称', '年齢': 'age'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['class'] = 'form-control'