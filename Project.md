Introduction
Group members: Sabrina Bhattarai, Matthew Gamboa, Md Billah

Django is a web framework. It is used in a number of HUGE sites including Youtube, Google search, Instagram, The New York Times, and Dropbox.
https://www.shuup.com/en/blog/25-of-the-most-popular-python-and-django-websites/

Reference material for learning the package can be found on the Django Website in Documentation
https://docs.djangoproject.com/en/1.9/intro/
Those are the tutorials we read through to get started.

In order to Understand Django, You should be able to read and write python. You should also learn how to read and use python Regular Expressions as they are needed to map urls in Django.

To save yourself from headaches involving dependencies, and to keep your workstation neat, you should set up a python virtual environment. Information on how to do that can be found here
http://docs.python-guide.org/en/latest/dev/virtualenvs/
And a Guide on reguar expressions can be found here 
https://docs.python.org/3/howto/regex.html
As stated before, they will be used to map urls (regex is used in string matching).

Installation:
<li>Step 1 :creating a virutal environment
		<p>A virtual environment is essentially an invisible folder which you can activate and deactivate.
		It allows us to have django or any programs we want to assosiate with a project in an environment.
		Our environment could have django 1.9 on it and will always work with group members so long as we pull up the environment. It elminitates the issues of us being on different versions of Django(if you were on 1.6 and I'm on 1.9, there could be some serious compatability issues in the project. Virtual environments elmininate this.</p>
		<ul>
			<li><em>virtualenv GroupDjango</em> This creates a virtualenvironment Named GroupDjango. 
			In it we can install any frameworks or libraries. We will soon use it to host our projects version of Django.</li>
			<li><em>source groupdjango/bin/activate</em> <---there is a different equivalent command for Windows
			<p>The above command will be used every time we want to reactiavte the virtual environment.
			(on this project, you must
			be in the directory in which your virtual environment was created) Youll know your in your virtual environment as on the left side of your terminal it will say (GroupDjango). To exit your virtual environment at any time, type <em>deactivate</em> into the terminal.</p>
			</li>
		</ul>
		<li>Step 2: Installing Django
			<p>cd into your environment folder and type <em>pip install Django</em></p></li>

		<li>Step 3: Create Project
		<em>django-admin startproject mysite</em> -----starts a project called mysite</li>

		<li><em>python manage.py runserver</em> ------this runs the server. Must be in the sites folder for this command to work.
		If you type 
		<em> http://localhost:8000/polls/</em>
			into your web browser, you can now view your project. </li>
		<li><em> python manage.py startapp polls</em> -----must be in directory where manage.py exists. polls is just the name of app. This creates an Application on your site. In the real world you will have several of these within a site.</li>

		from here on Your workflow involves setting up/ defining models, registering them to admin, and migrating those changes to a database.
		After that you edit urls, which lead to views, which are put into the page with templates.
Experiment:
	We essentially followed a couple of different tutorials and changed some of the output variables in order to create what we are currently showing you.
Source Code:
	Our code is all on Github(add link)

Conclusions:

	We could make very powerful dynamic websites using Django. The admin site which is built in to Django allows partners in our project to edit various models. We can set up a model and add or delete and edit individual objects within this admin site. Django also has a built in templating language (which is what allows it to be dynamic) in which we can "mix" python code with html. Django has built in form validation as well as various things to make your site more secure.

	Jobs in which you use Django are extremely high paying. Academically, we could use Django to host a website either locally or on the web. The possibilities are endless. The community is so large you can find several "ready-to-go" apps available for use. This can be extremely helpful in a large project as you can download those apps and edit them to your taste rather than starting completely from scratch.

##################Get it working on your comp

fork my repo, 
clone it, 
cd into its folder
type virtualenv . (this makes your current directory a virtualenv)
it will say its overwriting the old files (the ones that created my virtualenv)
cd .. 
when you type ls, you need to see the main project folder(the DjangoProject folder)
now type
source djangoproject/bin/activate (or the windows equivalent) Md, matthew knows this so he could send it to you

now cd into the project again.  You will see Group, manage.py, requirements.txt all those files and some more
type pip install -r requirements.txt
if the requirements are not already satisfied(which they may be) then it will download them to your virtualenv.

NOW your project is setup. Anytime you wish to work in it you must activate your virtualenvironment

