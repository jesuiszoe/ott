from django.contrib import admin
from .models import Netflix
from .models import *
# Register your models here.
admin.site.register(Netflix)
admin.site.register(Amazon)
admin.site.register(Hulu)
admin.site.register(Disney)


