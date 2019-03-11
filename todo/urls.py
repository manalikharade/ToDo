from django.config.urls import patterns,urls,path
from todo import views 
urlpatterns=[
	path('admin/',admin.site.urls),
	#path('/login',include('django.contrib.auth.urls'),name='login'),
	path('index/',views.index,name='index'),
	path('SignIn/',views.SignIn,name='SignIn'),
	path('SignUp/',views.SignUp,name='SignUp'),
	path('list/',views.list,name='list'),
	path('edit/',views.Edit,name='Edit')
]