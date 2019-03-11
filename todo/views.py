from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from .models import User,ToDo
# Create your views here.

def index(request):
	if(request.method == "POST"):
		if request.POST.get('login'):
			return render(request,'login.html')
		else:
			return render(request,'register.html')
	

def SignIn(request):
	user_obj=User.objects.filter(user=request.POST.get('username'),pwd=request.POST.get('password'))
	if(user_obj.count()):
		request.session['user_id']=user_obj[0].id
		request.session['user']=user_obj[0].user
		todos = ToDo.objects.filter(user_id=request.session['user_id'])
		return render(request,'list.html',{"user":request.session['user'],'todos':todos})
	else:
		return render(request,'home.html')

def SignUp(request):
	if(request.method == "POST"):
		MyLoginForm= LoginForm(request.POST)
		if(MyLoginForm.is_valid()):
			username=MyLoginForm.cleaned_data['username']
			password=MyLoginForm.cleaned_data['password']
			obj=User(user=username,pwd=password)
			obj.save()
	else:
		MyLoginForm=LoginForm()
	return render(request,'login.html')

def list(request):
	todos=ToDo.objects.filter(user_id=request.session['user_id'])
	if request.method=='POST':
		if 'listAdd' in request.POST:
			todo_obj=ToDo.objects.create(name=request.POST['listname'],duedate=str(request.POST['listdate']),user_id=request.session['user_id'])
			todos=ToDo.objects.filter(user_id=request.session['user_id'])
		elif 'listDelete' in request.POST:				
			try:
				checkedlist = request.POST.getlist("checkedbox")
				for list_id in checkedlist:
					todo=ToDo.objects.get(id=int(list_id))
					todo.delete()
			except:
				checkedlist = ''
			todos=ToDo.objects.filter(user_id=request.session['user_id'])
		elif 'listEdit' in request.POST:
			todo_obj=request.POST.getlist("checkedbox")
			if(len(todo_obj) < 2):
				item=ToDo.objects.get(id=int(request.POST.get('checkedbox')))
				return render(request,'edit.html',{'listItem':item})
		else:
			todos=ToDo.objects.filter(user_id=request.session['user_id'])
		
	return render(request,'list.html',{"user":request.session['user'],'todos':todos})

def Edit(request):
	if request.method == "POST":
		if 'save' in request.POST:
			ToDo.objects.filter(id=int(request.POST['save'])).update(duedate=str(request.POST['newDueDate']),name=request.POST['listName'])
	todos = ToDo.objects.filter(user_id=request.session['user_id'])
	return render(request,'list.html',{"user":request.session['user'],'todos':todos})

