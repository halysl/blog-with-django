from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,'blog/index.html',context={
			'title':'我的博客首页',
			'welcome':'welcome visit my web'
		})
