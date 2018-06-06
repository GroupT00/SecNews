#!/use/bin/python
#-*-coding:utf-8-*-
from django.db import models
class NewsSql(models.Model):
	Art_title = models.CharField(u'标题',max_length=255)
	Art_time = models.DateTimeField(u'时间',auto_now = True)
	Art_click = models.CharField(u'点击量',max_length=10,default=000)
	Art_type = models.IntegerField(u'分类',max_length=20,choices=((0,u'前端安全'),(1,u'后端渗透'),(2,u'漏洞分析'),(3,u'夺旗竞赛'),(4,u'神器分享'),(5,u'程序之美')))
	Art_url = models.CharField(u'链接',max_length=255)
	Art_exa = models.BooleanField(u'发布',default=True)
	def __unicode__(self):
		return u'%s -> %s' %(self.Art_title,self.Art_type)
