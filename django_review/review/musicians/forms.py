# 장고에서 미리 정의해둔 forms 받아오기
from django import forms 
# models에서 정의한 Musician 객체(class) 받아오기
from .models import Musician


# 클래스 정의
class MusicianForm(forms.ModelForm):
    # 클래스에 대한 클래스
    class Meta:
        # 어떤 모델? Musician에 정의된 것
        model = Musician
        # fields = ['name','age'] - input tag를 만들기 위함
        fields = '__all__'  # 모델에 정의한 모든 컬럼 불러올 수 있다.
        

