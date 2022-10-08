from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone 
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.urls import reverse 

STATUS = (
	('active','Chop_etildi'),
	('deactive','Qoralama')
)


# Create your models here.

class PublishMeneger(models.Manager): # new code
	def get_queryaet(self):
		return super().get_queryaet.filter(status='active')


class Post(models.Model):
	title = models.CharField(max_length=250, verbose_name="Sarlavha" )
	slug = AutoSlugField(populate_from="title")
	body = RichTextField(verbose_name="Matn")
	photo = models.ImageField(upload_to='post_photo/%Y/%m/%d/', verbose_name="Rasm")
	see = models.PositiveIntegerField(blank=True, null=True, verbose_name="Ko'rishlar soni")
	publish = models.DateTimeField(default=timezone.now, verbose_name="chop etilgan vaqt")
	status  = models.CharField(max_length=100, choices=STATUS, verbose_name="Holati")

	created_at = models.DateTimeField(auto_now_add=True, verbose_name="yaratilgan vaqti")
	updated = models.DateTimeField(auto_now=True, verbose_name="tahrirlangan vaqti")
	created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Muallif")

	objects = models.Manager()
	published = PublishMeneger()


	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post:post_detail', args=[self.id, self.slug])

	


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
	name = models.CharField(max_length=150)
	email = models.EmailField()
	body = RichTextField()
	created_at = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return self.name



