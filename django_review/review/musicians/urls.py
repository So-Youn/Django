from django.urls import path
from .import views # 경로에 따른 view함수 설정

# 어플리케이션 name space
app_name = "musicians"

# 장고 내부적으로 정해진 이름
urlpatterns = [
    # u - v - t 순서 고정.
    # path name을 무엇으로 지었는지, 어떤 view함수를 실행하는지 pattern 고정하기
    # 하나의 경로에 하나의 view함수!
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    # django가 지정한 경로 작성 방식
    # <데이터 타입 : 변수 명>
    # 실제 사용자가 작성하는 url
    # '3/'
    path('<int:musician_pk>/', views.detail, name="detail"),
    path('<int:musician_pk>/update/', views.update, name="update"),
    path('<int:musician_pk>/delete/', views.delete, name="delete"),


]