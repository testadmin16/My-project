from django.urls import path
from .views import list_view, detail_view, post_share,about_view,contact_view

app_name = "post"

urlpatterns = [
	path('<int:id>/share/', post_share, name="post_share"),
	path('<int:id>/<slug:slug>/', detail_view, name='post_detail'),
	path('about/', about_view, name='about'),
	path('contact/', contact_view, name='contact'),
	path('', list_view, name='post_list'),
]

