from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import PostShareForm, CommentForm
from django.core.mail import send_mail


def list_view(request):
	posts = Post.objects.filter(status='active')

	# pageinator ---------------------------------->>>>
	paginator = Paginator(posts, 9)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	# pageinator ---------------------------------->>>>
	
	return render(request, 'post/list.html', {'posts':posts, "page":page})


def detail_view(request,id, slug):
	post = get_object_or_404(Post, id=id, slug=slug)
	
	# activ commentlar "comments" o'zgaruvchisiga yig'ib olinadi
	comments = post.comments.filter(active=True)
	new_comment = None
	if request.method == 'POST':
		# Foydalanuvchi uchun izoh qoldirish formasi ko'rinadi
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			# Biz comment yaratamiz, lekin uni hali ma'lumotlar bazasida saqlamaymiz
			new_comment = comment_form.save(commit=False)
			# Joriy maqolaga sharh qo'shish.
			new_comment.post = post
			# commentni malumotlar bazasiga saqlaymiz 
			new_comment.save()
	else:
		comment_form = CommentForm()

	context = {'post':post,
			'comments':comments,
			'new_comment':new_comment,
			'comment_form':comment_form,
			}

	return render(request, 'post/detail.html', context)



def post_share(request, id):
	# id bo'yicha maqola olinadi
	post = get_object_or_404(Post, id=id)
	sent = False
	if request.method == 'POST':
		# forma saqlash  uchun yuboriladi
		form = PostShareForm(request.POST)
		if form.is_valid():
			# barcha maydonlar tasdiqlandi
			cd = form.cleaned_data
			
			post_url = request.build_absolute_uri(post.get_absolute_url())
			email = cd['email']
			subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
			message = 'Read "{}" at {}\n\n{}\'s comment:{}'.format(post.title, post_url, cd['name'], cd['comment'])
			send_mail(subject, message, email, [cd['to']])
			sent = True
	else:
		form = PostShareForm()

	context = {'post': post, 'form': form, 'sent': sent}

	return render(request, 'post/share.html', context)

def about_view(request):
	return render(request, 'about.html')


def contact_view(request):
	return render(request, 'contact.html')

