from django.http import HttpResponse
from django.shortcuts import render
from Sec_News.models import NewsSql
def submit(request):
	if request.POST:
		context = {}
		Art_Info = {}
		Art_Info['Art_url'] = request.POST['Art_url']
		Art_Info['Art_title'] = request.POST['Art_title']
		Art_Info['Art_type'] = request.POST['Art_type']
		context['alert'] = 'alert`Submit Success`'
		addArt_Info = NewsSql(Art_url=Art_Info['Art_url'],Art_title=Art_Info['Art_title'],Art_type=Art_Info['Art_type'],Art_exa=False)
		addArt_Info.save()
		return render(request, 'submit.html',context)
	return render(request, 'submit.html')
