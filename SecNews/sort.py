#!/use/bin/python
#-*-coding:utf-8-*-
from django.http import HttpResponse
from django.shortcuts import render
from Sec_News.models import NewsSql
from django.core.paginator import Paginator, PageNotAnInteger
def sort(request,taskid):
	Art = NewsSql.objects.all().filter(Art_exa=True).filter(Art_type=taskid)
	paginator = Paginator(Art[::-1],3)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
		contacts = paginator.page(1)
	except EmptyPage:
		contacts = paginator.page(paginator.num_pages)
		print type(contacts)
	return render(request,'index.html',{'contacts': contacts})
