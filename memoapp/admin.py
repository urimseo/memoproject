from django.contrib import admin

from .models import Memo, Comment
# Register your models here.
admin.site.register(Memo)
admin.site.register(Comment)