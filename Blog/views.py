from django.shortcuts import render
#from django.http import HttpResponse
from .models import Post

post=[
	{
		'Author': 'Anubhav Jain',
		'Title':'About Blogs',
		'Content':'ifud6lflf67',
		'Date_Posted':'05-July-2019 21:18'
	}
]


# Create your views here.

def home (request):
	#return HttpResponse('<h1>This is my first Web Page</h1>')
	return render(request,'Blog/Home.html')
	context={
		'Posts':Post.objects.all()
	}

def view_form (request):
	#return HttpResponse('<h1>This is Registration Page</h1>')
	return render(request, "Blog/Form.html")

