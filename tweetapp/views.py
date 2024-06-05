from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import Http404
from django.template import loader

from .models import User, Content
from .forms import ContentForm

# 初期表示
def index(request):
    content = Content.objects.select_related('usr_id')
    context = {
        'content': content
    }
    return render(request, 'tweetapp/index.html', context)

# 詳細表示
def detail(request, pk):
    content = Content.objects.select_related('usr_id').get(id=pk)
    context = {
        'content': content
    }
    return render(request, 'tweetapp/detail.html', context)

# 新規投稿
def create(request):
    if request.method == "POST":
        form = ContentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('tweetapp:index')
    
    else: 
        form = ContentForm()
        context = {'form': form, 'text': '新規投稿' }
        return render(request, 'tweetapp/create.html', context)

# 更新
def update(request, pk):
    obj = Content.objects.select_related('usr_id').get(id=pk)
    initial_values = {"id": obj.id, 
                      'usr_id': obj.usr_id , 
                      'tw_date': obj.tw_date, 
                      'tw_time': obj.tw_time, 
                      'content': obj.content }
    form = ContentForm(initial_values)
    context = {
        "form": form,
        "text": '更新',
    }
    return render(request, 'tweetapp/create.html', context)

# 投稿削除
def delete(request, pk):
    if request.method == 'POST':
        obj = Content.objects.get(id=pk)
        obj.delete()
        return redirect('tweetapp:index')
    
    else:
        obj = Content.objects.get(id=pk)
        context = {
            'content': obj
        }
        return render(request, 'tweetapp/delete.html', context)