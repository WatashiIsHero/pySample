from django.urls import path
from . import views

app_name = 'tweetapp'

urlpatterns = [
    path('', views.index, name='index'), # 一覧ページ
    path('<int:pk>', views.detail, name='detail'), # 詳細ページ
    path('create/', views.create, name='create'), # 新規投稿ページ
    path('<int:pk>/update/', views.update, name='update'), # 編集ページ
    path('<int:pk>/delete/', views.delete, name='delete'), # 削除ページ
    path('createuser/', views.createuser, name='createuser'), # ユーザ作成ページ
]
