from django.db import models

# Create your models here.
# 객체 생성 (클래스 생성)  > 테이블 명
class Musician(models.Model):
    # 멤버 변수  ex] name = '이름이란'
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
    # 인스턴스 호출 시 출력 내용 덮어쓰기
    def __str__(self):
        return f'{self.name}({self.age})'

class Album(models.Model):
    # Musician과의 1:N 관계
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.musician}-{self.title}'

