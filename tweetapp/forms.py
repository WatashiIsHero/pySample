from django import forms
from .models import User, Content

# def getChoises():
#     choises = User.objects.all()
#     choiseDict = {}
#     for choise in choises:
#         choiseDict[choise.id] = choise.name
#     return choiseDict

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['id', 'usr_id', 'tw_date', 'tw_time', 'content']
        labels = {'id':'投稿ID', 'usr_id':'ユーザ名', 'tw_date':'投稿日付', 'tw_time':'投稿時刻', 'content':'内容'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)