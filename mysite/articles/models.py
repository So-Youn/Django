from django.db import models

# Create your models here.
class Article(models.Model): # articles_article
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 자동으로 생성되는 시간 추가
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째글 - {self.title} : {self.content}'
        


