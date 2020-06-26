from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser



# Usercustomizing
class User(AbstractUser):
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="followings",
        blank=True,
    )


    # 각종 필드 추가
    # createsuperuser - 비어있는 계정 있어서 추가할 수 없다.
    # shell_plus => create_user, is_staff, 최고 권한 True
