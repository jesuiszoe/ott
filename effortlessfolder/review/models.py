from django.db import models

# Create your models here.

#글의 제목, 내용, 작성일, 마지막 수정일 
#balnk = False > 기본 옵션 인자- 폼에 빈칸 허용할지 설정
class Post(models.Model):
    title = models.CharField(max_length=50, unique =True, error_messages={'unique':'이미 있는 제목입니다.'})
    content = models.TextField(null=True)
    dt_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified", auto_now = True)

    def __str__(self):
        return self.title

