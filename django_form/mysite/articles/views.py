from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST) # Post일 때 인스턴스 생성 - 사용자가 보내온 정보를 담고있다
        if form.is_valid() : # 폼이 유효한지 확인하는 작업
            # article = Article.objects.get(pk=pk)
            # form에 담긴 정보가 ArticleFormdlrh
            # ArticleForm은 Article의 정보를 가지고 있다.
            article = form.save()
            return redirect('articles:index')
    else :
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    articles = Article.objects.get(pk=article_pk) # 특정 게시글 조회 (instance)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=articles)
        if form.is_valid(): # 유효성 검사
            articles = form.save()
            return redirect('articles:index')
    else :
        form = ArticleForm(instance=articles)
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context) 

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # request.resolver_match : 작성된 url을 번역해준다.
    # request.resolver_match.url_name >>> detail 출력
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)