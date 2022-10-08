from django.contrib import admin
from .models import Post, Comment

# Register your models here.

# 1-usul
# admin.site.register(Post)



# 2-usul
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','id','slug','see','publish','status', 'created_by')
	list_filter = ('publish','status','created_by')
	search_fields = ('title','body')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'active', 'created_at')
	list_filter = ('active','created_at')
	search_fields = ('name','body','email')
	list_editable  = ('active',)






