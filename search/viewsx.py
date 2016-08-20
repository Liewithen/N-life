# -*- coding: utf-8 -*-
import re
import hashlib
import requests
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect





#成绩正则
def Deal_grade(pageCode):
	pattern = re.compile('<tr>.*?<td>(.*?)</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td align="left">(.*?)</td>.*?'+
						 '<td align="left">(.*?)</td>.*?'+
						 '<td style=".*?">(.*?)</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td>(.*?)</td>.*?'+
						 '<td>(.*?)</td>.*?</tr>',re.S)
	items = re.findall(pattern,pageCode.decode('utf-8'))
	return items
# 课表正则
def Deal_course(pageCode):


	pattern = re.compile('<div.*?-2" style="display: none;.*?>(.*?)</div>',re.S)
	items = re.findall(pattern,pageCode.decode('utf-8'))
	removeBR = re.compile('<br/>|<br>')
	removeTag = re.compile('<.*?>')
	removeNbsp = re.compile('&nbsp;')
	temp_items = []

	#清除无关标签
	def tool(x):
		x = re.sub(removeBR,"\n",x)
		x = re.sub(removeTag,"",x)
		x = re.sub(removeNbsp,"",x)
		return x

	for item in items:
		temp_items.append(tool(item))

	return temp_items


def index(req):
	return render_to_response('index.html',{})

def info(req):
	if req.method == 'POST':
		username = req.POST['username']
		password = req.POST['password']
		m = hashlib.md5()
		m.update(password)
		psw = m.hexdigest()
		pwd = psw.upper()
		url = 'http://202.119.81.113:9080/njlgdx/xk/LoginToXk?method=verify&USERNAME='+username+'&PASSWORD='+pwd
		s = requests.Session()
		r = s.get(url)
		if r.url == 'http://202.119.81.113:9080/njlgdx/framework/main.jsp':


			#正则获取用户名
			pageCode = r.content.decode('utf-8')
			pattern = re.compile('<div id="Top1_divLoginName".*?>(.*?)</div>',re.S)
			items = re.findall(pattern,pageCode)


			#正则获取用户成绩
			data_grade = {'kksj':'','kcxz':'','kcmc':'','xsfs':'max',}
			req_grade = s.post('http://202.119.81.113:9080/njlgdx/kscj/cjcx_list',data=data_grade)
			items_grade = Deal_grade(req_grade.content)


			#正则获取用户课表
			data_course = {'cj0701id':'','zc':'','demo':'','xnxq01id':'2016-2017-1'}
			req_course = s.post('http://202.119.81.113:9080/njlgdx/xskb/xskb_list.do?Ves632DSdyV=NEW_XSD_PYGL',data=data_course)
			items_course = Deal_course(req_course.content)

			#正则获取用户考试信息(待开发)
			#req_exam = s.get('http://202.119.81.113:9080/njlgdx/xsks/xsksap_list')

			return render_to_response('info.html',{'name':items[0],'grade':items_grade,'course':items_course})

		else:

			return HttpResponseRedirect('/index/')
	else:
		return HttpResponseRedirect('/index/')

