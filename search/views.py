# -*- coding: utf-8 -*-
import re
import hashlib
import requests
import time
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
#成绩正则
@csrf_exempt
def Deal_grade(pageCode):
	pattern = re.compile('<tr>.*?<td>.*?</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td align="left">.*?</td>.*?'+
						 '<td align="left">(.*?)</td>.*?'+
						 '<td style=".*?">(.*?)</td>.*?'+
						 '<td>.*?</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td>.*?</td>.*?'+
						 '<td>.*?</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td>.*?</td>.*?</tr>',re.S)
	items = re.findall(pattern,pageCode.decode('utf-8'))
	return items
# 课表正则
@csrf_exempt
def Deal_course(pageCode):


	pattern = re.compile('<div.*?-2" style="display: none;.*?>(.*?)</div>',re.S)
	items = re.findall(pattern,pageCode.decode('utf-8'))

	return items

@csrf_exempt
def index(req):
	return render_to_response('index.html')

@csrf_exempt
def info(req):
	if req.method == 'POST':
		username = req.POST['username']
		password = req.POST['password']
		#headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }  
		m = hashlib.md5()
		m.update(password)
		psw = m.hexdigest()
		pwd = psw.upper()
		url = 'http://202.119.81.113:9080/njlgdx/xk/LoginToXk?method=verify&USERNAME='+username+'&PASSWORD='+pwd
		s = requests.Session()
		r = s.get(url)
		if r.url == 'http://202.119.81.113:9080/njlgdx/framework/main.jsp':


			#正则获取用户信息
			pageCode = r.content.decode('utf-8')
			pattern = re.compile('<div id="Top1_divLoginName".*?>(.*?)</div>',re.S)
			items = re.findall(pattern,pageCode)


			#正则获取用户成绩
			data_grade = {'kksj':'','kcxz':'','kcmc':'','xsfs':'max',}
			req_grade = s.post('http://202.119.81.113:9080/njlgdx/kscj/cjcx_list',data=data_grade)
			items_grade = Deal_grade(req_grade.content)


			#正则获取用户课表

			WeekNumber = time.strftime('%W',time.localtime(time.time()))
			zc = int(WeekNumber) - 33
			if zc <= 0:
				zc = 1
			if zc >= 30:
				zc = 30
			data_course = {'cj0701id':'','zc':str(zc),'demo':'','xnxq01id':'2016-2017-1'}
			req_course = s.post('http://202.119.81.113:9080/njlgdx/xskb/xskb_list.do?Ves632DSdyV=NEW_XSD_PYGL',data=data_course)
			items_course_all = Deal_course(req_course.content)

			#正则获取用户考试信息(待开)
			#req_exam = s.get('http://202.119.81.113:9080/njlgdx/xsks/xsksap_list')

			return render_to_response('info.html',{'name':items[0],'grade':items_grade,'course_all':items_course_all,'zc':zc})

		else:

			return HttpResponseRedirect('/index/')
	else:
		return HttpResponseRedirect('/index/')

