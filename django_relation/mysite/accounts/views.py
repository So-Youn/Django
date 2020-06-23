from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# from django.contrib.auth import UserChangeForm as CustomUserChangeForm
# views.py 내 정의한 함수 login과 구분하기 위해 auth_log로 재 명명함
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CustomUserChangeForm 
from .forms import UserPassChangeForm

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST) # request : 요청 파라미터
            # AuthenticationForm은 ModelForm이 아닌 Form 상속
            # 별도로 정의된 Model이 없다는 뜻
            # 그래서 넘겨주는 인자가 달라진다.
        if form.is_valid():
            # 로그임은 DB에 뭔가 작성하는 것은 동일하지만, 
            # 연결된 모델이 있는 건 아닙니다.
            # 그럼 무엇을 확인해야 하는가?  - 세션과 유저 정보
            auth_login(request, form.get_user()) 
            return redirect("articles:index")
    else:
        if request.user.is_authenticated :
            return redirect("articles:index")
        else:
            form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, "accounts/form.html", context )

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST) # 사용자가 POST방식으로 보내온 정보를 담아서 form 생성
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("accounts:login")

    else:
        form = UserCreationForm() # 인스턴스화
    context = {
        'form' : form
    }
    return render(request, 'accounts/form.html', context)

def logout(request):
    auth_logout(request)
    return redirect("articles:index")

# 회원 삭제
@require_POST # 삭제는 POST일 때만 가능 - get방식으로 들어 왔을 때는 405에러 
def delete(request):
    request.user.delete()  # request안에 요청을 보낸 user의 데이터가 들어있어서 다른 매개변수는 필요 없다.
    return redirect('articles:index')

def update(request):
    if request.method =="POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            return redirect("articles:index")
    else:
        form =  CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/form.html', context)

@login_required
def password(request):
    if request.method == "POST":
        form = UserPassChangeForm(request.user, request.POST) # 순서 꼭 지키기
        if form.is_valid():
            user = form.save()
            # auth_login(request, user) - 저장되어있던 session이 바뀌고 새로운 session을 만든다.
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = UserPassChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/form.html', context)