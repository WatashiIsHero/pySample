from django.shortcuts import render
from tweet.models import User, Content
from django.views import generic

# IndexViewクラス作成
class IndexView(generic.ListView):
    model = Content
    template_name = 'tweet/tweet.html' # ビュー指定

# def tweetData(request):
#     contents = Content.objects.all()
#     context = {
#         'contents': contents,
#     }
#     return render(request, 'tweet/tweet.html', context)