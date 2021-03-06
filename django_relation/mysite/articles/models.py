from django.db import models
from django.conf import settings
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail



# Create your models here.

def articles_image_path(instance, filename):
    return f'user_{instance.user.pk}/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    # blank - 유효성 검사 시
    # null - DB상의 컬럼의 Null
    image = models.ImageField(blank=True, upload_to="%y/%m/%d/") # 업로드 날짜별 저장
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200,300)],
        format='JPEG',
        options={'quality':90},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     # 게시글 좋아요
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_articles',
        blank=True) # 게시글에 좋아요 없는 유효성 검사 통과할 수 있도록 blank=True 걸어준다.
    recommend_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='recommend_articles',
        blank=True)


    # Article이 호출되었을 때 출력되는 내용 - magic method
    def __str__(self):
        return f'{self.pk}번째 글, {self.title}-{self.content}'

class Comment(models.Model):
    # 멤버 변수 = models.외래키(참조하는 객체, 삭제 되었을 때 처리 방법[on_delete])
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE)
    # 역참조 값 설정 related_name = 'comments'
    content = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   
    

    def __str__(self):
        return f'Article:{self.article},{self.pk}-{self.content}'