from django.contrib import admin
from .models import Netflix
from .models import *
# Register your models here.
# 어드민 페이지에서 데이터베이스 조회
admin.site.register(Netflix)
admin.site.register(Amazon)
admin.site.register(Hulu)
admin.site.register(Disney)


