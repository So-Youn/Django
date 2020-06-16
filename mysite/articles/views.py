from django.shortcuts import render, redirect
# 모델 가져오기
from .models import Article

# Create your views here.
def index(request):
     # 전체 데이터 가져오기
    articles = Article.objects.all()[::-1]
    # 그 데이터를 템플릿에게 넘겨주기
    context = {
        'articles' : articles
    }
    
    # 템플릿에서 반복문으로 각각의 게시글의 pk, title 보여주기
    return render(request, 'articles/index.html',context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 데이터 생성을 위한 ORM 활용
    # 첫번째 방법
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 어떤 방식을 사용했는가에 따라서
    # SAVE() 메서드를 사용할 것인지 아닌지
    # 두번째 방법
    # article = Article(title=title,content=content)
    # article.save()
    article = Article.objects.create(title=title,content=content)
    # context = {
    #     'title' : title,
    #     'content' : content
    # }
    # return render(request, 'articles/index.html', context)
    return redirect('articles:index')

def introduce(request):
    return render(request, 'articles/introduce.html')

# 1. 상세 페이지를 보기 위한 경로
# 1-1. 특정 게시들에 대한 고유 값
# 1-2. /articles/1/, /articles/2/
# 2. 해당 게시글에 대한 상세 내용
# 3. 인덱스 페이지로 돌아가는 링크

def detail(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article 
    }
    return render(request, 'articles/detail.html',context)

# 1. 특정 글 삭제를 위한 경로 작성
# 1-1. /articles/1/delete
# 2. 글 삭제 처리를 해주는 View 작성
# 3. 글 삭제 후, index page로 redirect
# 4. 글 삭제를 위한 링크 detail에 작성
def delete(request, delete_pk):
    # post 방식 : request.method
    article = Article.objects.get(pk=delete_pk)
    article.delete()
    return redirect('articles:index')

# 1. 특정 글 수정을 위한 경로 생성
# 1-1. /articles/1/edit/
# 2. 글 수정 template를 render하는 edit view 작성
# 2-1. 해당 template에 form tag 작성
# 2-3. 각 input tag 내부에 기존 내용이 들어있어야 함.
# 2-3. value 속성을 활용
def edit(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request,'articles/edit.html',context)

# update
# 3. edit에서 보낸 데이터 처리를 위한 경로 생성
# 3-1. /articles/1/update
# 4. 글 수정 처리를 하는 update view 작성
# 5. 해당 글 상세 페이지로 redirect
# 6. 글 수정을 위한 edit 링크 상세 페이지 설정
# 6-1. {% url 'articles:edit' article.pk %}
def update(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail',article_pk)