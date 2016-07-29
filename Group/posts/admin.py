from django.contrib import admin
from .models import Post	 #imports Post class
# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title","timestamp","update"] 
	list_display_links = ['update','timestamp']
	list_filter = ['update','title','timestamp']
	search_fields = ['title','content']
	list_editable = ['title']
		#these parameters are all defined in models. adding them to list_display allows them to be viewed
		#and changed via the admin
	class Meta:
		model =  Post #connects this class to Post
admin.site.register(Post,PostModelAdmin) #registers post into admin site