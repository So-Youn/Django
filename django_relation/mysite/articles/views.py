from django.shortcuts import render, redirect, get_object_or_404
# DVDH
# Django가 주는 views에서 쓸 decorators http를 위함
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment_form = CommentForm()
    comments = article.comment_set.all() # 특정 article이 가지고 있는 댓글 조회
    # 1: N을 보장할 수 없기 때문에 querySet(commet_set)형태로 조회해야 한다.
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments' : comments
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == "POST":
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


# def comment_delete(request, article_pk, comment_pk):
#     # article_id: 게시글에 대한 pk 값
#     comment = get_object_or_404(Comment, pk=comment_pk) # Comment : model에서 정의한 class
#     if request.method == "POST":
#         comment.delete()
#     return redirect('articles:detail', article_pk) # comment.article.pk - OK
@require_POST
def comment_delete(request, article_pk, comment_pk):    
    comment = get_object_or_404(Comment, pk=comment_pk) # Comment : model에서 정의한 class
    comment.delete()
    return redirect('articles:detail', article_pk) # comment.article.pk - OK
    
def insert(request, article_pk):
    # article = Article.objects.get(pk=article_id)
    article = get_object_or_404(Article, pk = article_pk)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)   # 이로서 접근 권한이 생김
            # commit=False ?  생성은 하지만 DB에 반영은 하지 않는다 default는 True 
            # comment = article.comment_set.all() 
            #comment.article_id = article.pk 
            comment.article = article
            comment.save()
            return redirect('articles:detail', article.pk)
        else:
            context = {
                'comment_form': focomment_form,
                'article' : article
            }
    return render(request, 'articles/detail.html', context)




