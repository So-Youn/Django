from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content
    }
    return render(request, 'articles/create.html', context)
def introduce(request):
    return render(request, 'articles/introduce.html')
# 1. /introduce/
# 2. h1태그로 이루어진 제목
# 3. back링크로 index로 돌아갈 수 있는 링크 하나
# 4. index에서 introduce로 이동할 수 있는 링크 하나