from django import template
from django.db.models import Count
from ..models import Post


register  = template.Library()

@register.inclusion_tag('tags/lastest_posts.html')
def show_lastest_posts(count=5):
    lastest_posts = Post.objects.filter(status = 'active').order_by('-created_at')[:5]
    return{'lastest_posts': lastest_posts}
    
@register.inclusion_tag('tags/more_view.html')
def show_more_view(count=5):
    more_view = Post.objects.filter(status = 'active').order_by('-see')[:5]
    return{'more_view': more_view}
    