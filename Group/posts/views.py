from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post


def post_create(request):
	#if request.method == "POST":
		#print(request.POST.get('title'))
		#print(request.POST.get('content'))
		#Post.objects.create('title'=title)
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Message Saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {'form': form}
	return render(request, 'post_form.html', context)
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
	#return HttpResponse('<h1>list/Home</h1>')
def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id) #gets a post based on its id
	form = PostForm(request.POST or None, instance=instance) #brings up the form with its writing in it(this is done by instance = instance)
	if form.is_valid(): #if form button is pushed and its valid, this all happens (basically it saves it to db)
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Everything is working!!!!!!") #posts a message after redirect
		return HttpResponseRedirect(instance.get_absolute_url()) #redirects us to absoluteURl of instance, which is just post_detail w that instances id args
	context = {"title": instance.title,
				"instance": instance,
				"form":form,}
	return render(request, 'post_form.html', context)#p1 request p2 template p3 dictionary(used in templates)
def post_delete(request, id=None): #create a button leading to this url (which would call the function)
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"Post Deleted") #not defined in our list template yet
	return redirect("posts:list")
	
