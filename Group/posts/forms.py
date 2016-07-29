from django import forms
from.models import Post #or whatever your model is called

class PostForm(forms.ModelForm):
	class Meta:
		model = Post #links to our post model
		fields = ['title','content']	#these fields come from model also, they are ones we wish to put in form