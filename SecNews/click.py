from django.http import HttpResponse
from django.shortcuts import render
from Sec_News.models import NewsSql
def click(request):
	if 'id' in request.GET:
		tid = NewsSql.objects.get(pk=request.GET['id'])
		tid.Art_click = int(tid.Art_click)+1
		tid.save()
		return HttpResponse('')
	else:
		return HttpResponse("Hello world ! ")

