# django relation 1:N
---
## CREATE
```python
# 1. 댓글 생성
comment = Comment()
comment.content = '첫번째 댓글'
comment.save()

# 2. 게시글 하나 불러오기
article = Article.objects.get(pk=1)

# 2-1. comment와 article 연결하기
comment.article = article
comment.save()

# 또 다른 방법
# 작성하는 숫자는 참조하는 게시글 article의 pk 값
# 주의 :  article_pk 사용 불가 
comment.article_id = 1
comment.save()
```

## READ
```python
# comment 변수들 불러오기
# 1. 댓글 번호 조회
comment.pk

# 2. 댓글 content 조회
comment.content

# 3. 댓글이 어느 게시글에 연결되어 있는가.
comment.article_id

# 4. 댓글이 연결된 게시글
comment.article

# 4-1. 댓글이 연결된 게시글의 제목과 내용
comment.article.pk
comment.article.title
comment.article.content


# article의 경우는 ? 
article.comment_set.all() # 게시글이 가지고 있는 전체 댓글 조회 - QuerySet 형태 
# QuerySet ? -  반복문으로도 사용이 가능하다.

# comment_set 댓글을 몇개 가지고 있는지 특정지을 수 없기 때문에 comment_set 사용
# comment와 달리 직접 접근을 할 수 없다.


``` 