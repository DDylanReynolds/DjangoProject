Create an app, add it to settings.py
###notes to self
change timezone in settings.py
in polls app we used more than just appname in INSTALLED_APPS, why?
check out CRUD on wikipedia, get,post,put,delete
#compare the render methods I used on this vs other (shortcut vs reg)

for Djangoproject
1) pip install django inside the virtualenv
2)django-admin startproject Group
3)cd into it, then python mange.py runserver #it will say unapplied migrations
4)python manage.py migrate
5)python mange.py createsuperuser BOSS/grouppass

######Create APP
6) python manage.py startapp posts #creates app called posts which comes with its set of files and folers
7)edit posts.models.py. 
 
add a class with parameter model.models.Model
inside the class create a function named __str__(self) 
										return self.one of variables to get readable text
								##if we did not include this, we could not read words on admin.py

8)under installed_apps (in settings.py) add the appname. in our case 'posts'
9) python manage.py migrate. works, but basically says the db and models aren't in sync. to fix this run
10)python manage.py makemigrations #django now sees changes, but hasn't applied them
11) python manage.py migrate #now the changes have been applied

########Making the model viewable in admin
in admin.py
from models import the class, then register it to admin site by writing
admin.site.register(Post) instead of Post, write whichever class you wish to register

12)once it is registered, I can view AND EDIT the model via admin interface

##########Customizing admin interface
	create a class in admin.py with admin.ModelAdmin as parameter 
	and write class Meta:
					model = class were linking it to
ex ## class PostModelAdmin(admin.ModelAdmin):
			list_display['modelparamater1','modelparameter2']
			class Meta:
				model= Post ###don't forget to include this class in the regester admin function as before
adding things to list_display allows us to see and edit them in admin. The parameters are variable within the class defined in models <a>https://docs.djangoproject.com/en/1.9/ref/contrib/admin/</a>
list_display_links[] make things in it clickable/changeable. must be defined in list_display for this to work
list_filter[] adds filter to admin
serach_fields[] allows you to add a search bar to admin
list_editable=[] makes them editable. check out all the others for model admin in
 <a>https://docs.djangoproject.com/en/1.9/ref/contrib/admin/</a>

 ###############views
 views.py (oftheapp)
 there are class based views and function-based views. We will first learn function-based(class is more advanced)

 1) if using http response, add from django.http import HttpResponse
 2)create a function with request as parameter, and return an http response. ex
 def posts_home(request):
	return HttpResponse(<h1>'I am posts_home'</h1>)
	then to urls.py/urlpatterns add #url(r'nameinadressbarw/regex,'<appname>.views.functionname') 
	to make it findable
#################mapping urls to views. Uses python regular expressions. I have a guide for common ones on my github

Basically, the urls.py under our main project folder will lead us to app names and should have include('appname.urls'). we must import this from the same place as urls.
This will lead us to the urlconfs under the app located in appname/urls.py
this 13/38 helps alot <a>https://www.youtube.com/watch?v=nw3R2TXlkwY&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy&index=12#t=26.966970407</a>

##################Setting up templates

create a folder on the same level as manage.py, any apps, and the main project.
call it templates and add an html file inside of it.

also, under Templates/dirs[] inside of settings.py, add 
os.path.join(BASE_DIR, 'templates')
the BASE_DIR is basically the main project level w/ manage.py, and templates is what we're adding. the code specifies a path to it that is indepenant of os path basically.

If i define a dictionary in a function in views.py, when doing render(request, 'template', dictionary)
I write the name of the dictionary used there. This allows me to use the dictionary "keys" in templates.
if i have "title" = "BLALA" and I write {{title}} then my page wil have blabla

writing #if request.user.is_authenticated(): then changing the context variable based on if-else statements is doable. the if-else lives inside the function in views. the #if request.user.is_authenticated(): will
do something if a user is logged in

###############Querysets    Querying database Models are found in models.py 

1) python manage.py shell ##(this opens basically another shell, but one that understands the django API)
do a full path import of your model
ex from posts.models import Posts
ex from appname.models import class

2) classname.objects.all() #this prints all the objects defined by that class that are IN THE DATABASE
ex Posts.objects.all()
I can also use .filter(varwithinclass = "whatever")
ex Posts.objects.filter('title'= Post1) will display any object titled Post1
to make it case insensitive write .filter(title__icontains = 'whatever title is')

I can also to .create(title = '', content='') once you fill in all the required parameters to that model you just press enter and it is created in the database

3) Update your views.py. import the class ex from .models import Post
	I can can save Post.objects.all() to a variable and add it to the rendered dictionary to display in on a page.
#####Super important!!!!!!!!!!
if i want to do loops in templates I must do {% for n in whatever%}
followed by {%endfor%} there is no need for indents in template, this is the loop syntax.

############# in views.py from django.shortcuts import get_object_or_404 
post.objects.get(id=1) or whatever the id of the thing i want to get is
write instance = get_object_or_404(Classname, id=3) #this will cause a 404 error page to raise
if the id isn't matched. You can use any of the classes subvariables as the second parameter ex title

Basically get get_object_or_404(class,idorsub) gets  the specific object. if the object doesn't exist, a 404 is shown.

save the object to a variable and I can now use it as well as its submethods to do things. I can choose to display certain parts via using its submethods and dictionaries/templates.


#######Dynamic url routing vid 18
the thing i add in url routing ex
url(r'^detail/(?P<id>\d$+)/$', post_detail), says if i have url detail/anid#/ call post_detail 
in views.py, post_detail(request), add the parameter id so its now post_detail(request, id)
now the id requested in the url is sent and I can use this info within my functions. id is now = whatever the url id says
#########url links/absolute urls

1) add a third parameter name= 'thename' to your urls
2) inside the include() add namespace = 'namespacename' afor a url that leads to several others (url that leads to post.urls.p for ex)
3) in the models folder of your app, add
from django.core.urlresolvers import reverse ##into models.py
def get_absolute_url(self):
		return reverse('posts:detail', kwargs={'id':self.id})
		--get_absolute url essentially returns a string that tells django how to deal with urls in a way
		that doesn't require them being hard coded.
		using reverse('namespace:name',any kwargs or args needed after)

4) when creating a link we can now write <a href="{{ object.get_absolute_url }}">{{ object.name }}</a>

########adding model forms
1) create a forms.py file inside the app.
	add from django import forms
	from.models import Post #or whatever your model is called
	2)createa class with parameters (forms.ModelForm):
	and inside that create class Meta:	
		model = modelname
		fields =["title","content"] #fields will hold the fields from our model we wish to make into forms
3) head to your views and import the class you created
ex from .forms import PostForm

now save it to a variable (this will allow us to use it in context)
ex form = PostForm() ##initializes class and saves it to variable
context = {"form": form}

{{form.as_p}} puts form in a paragraph(form is a variable)




