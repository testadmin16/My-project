from django import forms
from .models import Comment

class PostShareForm(forms.Form):
	name = forms.CharField(max_length=70)
	email = forms.EmailField()
	to  = forms.EmailField()
	comment = forms.CharField(required=False)


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','email','body')
		

