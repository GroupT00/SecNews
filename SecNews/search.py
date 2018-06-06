#!/use/bin/python
#-*-coding:utf-8-*-
from django.http import HttpResponse
from django.shortcuts import render
from Sec_News.models import NewsSql
from django.core.paginator import Paginator, PageNotAnInteger
def search(request):
	if 's' in request.GET:
		Art = NewsSql.objects.filter(Art_title__icontains=request.GET['s']) 
		paginator = Paginator(Art,15)
		page = request.GET.get('page')
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)
		return render(request,'index.html',{'contacts': contacts})
	else:
		Art = NewsSql.objects.all()
		paginator = Paginator(Art,15)
		page = request.GET.get('page')
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
			contacts = paginator.page(1)
		except EmptyPage:
			contacts = paginator.page(paginator.num_pages)
		return render(request,'index.html',{'contacts': contacts})
