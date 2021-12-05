from django.contrib import admin
from .models import Post
# Register your models here.
# 어드민 페이지에서 post 목록 조회
admin.site.register(Post)