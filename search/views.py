# -*- coding: utf-8 -*-
import re
import hashlib
import requests
import time
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
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
	if req.GET.get('message') == 'error':
		return render_to_response('index.html',{'error':'账号密码错误或教务处崩了'})
	else:
		return render_to_response('index.html',{'error':''})

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
			if zc <= 4:
				zc = 5
			if zc >= 30:
				zc = 30
			data_course = {'cj0701id':'','zc':str(zc),'demo':'','xnxq01id':'2016-2017-1'}
			req_course = s.post('http://202.119.81.113:9080/njlgdx/xskb/xskb_list.do?Ves632DSdyV=NEW_XSD_PYGL',data=data_course)
			items_course_all = Deal_course(req_course.content)

			#正则获取用户考试信息(待开)
			#req_exam = s.get('http://202.119.81.113:9080/njlgdx/xsks/xsksap_list')

			return render_to_response('info.html',{'name':items[0],'grade':items_grade,'course_all':items_course_all,'zc':zc})

		else:

			return HttpResponseRedirect('/index/?message=error')
	else:
		return HttpResponseRedirect('/index/')

def FindRoom(req):

	ZC = req.GET.get('zc')
	DAY = req.GET.get('day')
	JC = req.GET.get('jc')

	responseRoom = []

	def JudegJc(JC):
		if JC == 1:
			return 'oneisavl'
		if JC == 2:
			return 'twoisavl'
		if JC == 3:
			return 'threeisavl'
		if JC == 4:
			return 'fourisavl'
		if JC == 5:
			return 'fiveisavl'

	sql = 'select roomid from search_saow'+ZC+' where timeofday ='+DAY+' and '+JudegJc(int(JC))

	cursor = connection.cursor()
	cursor.execute(sql)

	roomid = cursor.fetchall()

	for r in roomid:
		responseRoom.append(r[0]+' ')
	return HttpResponse(responseRoom)


