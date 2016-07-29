from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post


def post_create(request):
	return HttpResponse('<h1>Update</h1>')
def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {"title":instance.title, "instance": instance,}
	return render(request, 'post_detail.html', context)
def post_list(request):
	#if request.user.is_authenticated():	 ##this if else function allows us to change 
	#whats sent to template based on whether or not a user is logged in.
	querySet = Post.objects.all() #this saves all my post objects to a variable so I can use them and
			#their methods within the dictionary and therefore in the templates too
	context = {"title": "List", "object_list": querySet}
	#else:
	#	context = {"title": "Noone Logged In"}
	return render(request,'index.html',context)
	#request, template link, dictionary are the parameters
	#return HttpResponse('<h1>List/Home</h1>')
def post_update(request):
	return HttpResponse('<h1>Update</h1>')
def post_delete(request):
	return HttpResponse('<h1>Delete</h1>')
