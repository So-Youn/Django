from django import forms
from .models import Article, Comment # models에서 객체 호출

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        #fields = '__all__'
        exclude = ['user','like_users', 'recommend_users']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = '__all__' #  __all__ : 전체 게시글 연결
        # fields = ['content'] 이렇게 작성하기에는 양이 너무 방대함.
        exclude = ['article', 'user'] # article만 제외하고 연결시킨다. 