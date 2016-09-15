#coding=utf-8
import re
import requests
import hashlib
ALL=['Ⅳ-A101',
'Ⅳ-A102',
'Ⅳ-A103',
'Ⅳ-A104',
'Ⅳ-A106',
'Ⅳ-A107',
'Ⅳ-A108',
'Ⅳ-A109',
'Ⅳ-A110',
'Ⅳ-A111',
'Ⅳ-A112',
'Ⅳ-A202',
'Ⅳ-A203',
'Ⅳ-A204',
'Ⅳ-A206',
'Ⅳ-A207',
'Ⅳ-A208',
'Ⅳ-A209',
'Ⅳ-A210',
'Ⅳ-A211',
'Ⅳ-A212',
'Ⅳ-A301',
'Ⅳ-A302',
'Ⅳ-A303',
'Ⅳ-A304',
'Ⅳ-A306',
'Ⅳ-A307',
'Ⅳ-A308',
'Ⅳ-A309',
'Ⅳ-A310',
'Ⅳ-A311',
'Ⅳ-A312',
'Ⅳ-A401',
'Ⅳ-A403',
'Ⅳ-A404',
'Ⅳ-A406',
'Ⅳ-A407',
'Ⅳ-A408',
'Ⅳ-A409',
'Ⅳ-A410',
'Ⅳ-A411',
'Ⅳ-A412',
'Ⅳ-A501',
'Ⅳ-A502',
'Ⅳ-A504',
'Ⅳ-A505',
'Ⅳ-A506',
'Ⅳ-A507',
'Ⅳ-A508',
'Ⅳ-A509',
'Ⅳ-A510',
'Ⅳ-B101',
'Ⅳ-B301',
'Ⅳ-B303',
'Ⅳ-B306',
'Ⅳ-B307',
'Ⅳ-B308',
'Ⅳ-B309',
'Ⅳ-B310',
'Ⅳ-B311',
'Ⅳ-B312',
'Ⅳ-B314',
'Ⅳ-B401',
'Ⅳ-B403',
'Ⅳ-B406',
'Ⅳ-B407',
'Ⅳ-B408',
'Ⅳ-B409',
'Ⅳ-B410',
'Ⅳ-B411',
'Ⅳ-B412',
'Ⅳ-B414',
'Ⅳ-B501',
'Ⅳ-B502',
'Ⅳ-B505',
'Ⅳ-B506',
'Ⅳ-B507',
'Ⅳ-B508',
'Ⅳ-B509',
'Ⅳ-B510',
'Ⅳ-B512',
'Ⅳ-C101',
'Ⅳ-C102',
'Ⅳ-C103',
'Ⅳ-C104',
'Ⅳ-C105',
'Ⅳ-C106',
'Ⅳ-C107',
'Ⅳ-C108',
'Ⅳ-C203',
'Ⅳ-C205',
'Ⅳ-C206',
'Ⅳ-C207',
'Ⅳ-C208',
'Ⅳ-C209',
'Ⅳ-C210',
'Ⅳ-C212']
def MD5(password):
	md5 = hashlib.md5()
	md5.update(password)
	psw = md5.hexdigest().upper()
	return psw

def PrintSQL(result,zc):
	RE_RoomId = '<tr>.*?<td height="28" align="center">.*?<nobr>(.*?)</nobr>.*?</td>.*?'
	RE_Course = '<td  height="28" align="center" valign="top">.*?<nobr>(.*?)</nobr>.*?</td>.*?'
	for count in range(35):
		RE_RoomId += RE_Course
	pattern = RE_RoomId + '.*?</tr>'
	classroom_list = re.findall(pattern,result.content,re.S)
	T = []
	for lists in classroom_list:
		num = 0
		temp = []
		for list in lists:
			if num == 0:
				temp.append(list)
			else:
				if re.search('</div>',list):
					temp.append(0)
				else:
					temp.append(1)
			num += 1
		T.append(temp)
	f=open(str(zc)+'.txt','w')
	for rooms in T:
		roomid = rooms[0]
		num = 0
		zc = 1
		for room in rooms:
			if num > 0:
				if num%5 == 1:
					print >>f,str(roomid)+', '+str(zc)+', 4, '+str(room)+',',
					zc += 1
				else:
					if num%5 == 0:
						print >>f,str(room)+'\n',
					else:
						print >>f,str(room)+',',
			num += 1
	for all in ALL:
		flag = 1
		for rooms in T:
			if all == rooms[0]:
				flag = 0
				break
		if flag == 1:
			for a in range(7):
				print >>f,all+', '+str(a+1)+', 4, '+'1, 1, 1, 1, 1'
username = input('username: \n')
password = input('password: \n')
pwd = MD5(str(password))
Session = requests.Session()
login_url = 'http://202.119.81.113:9080/njlgdx/xk/LoginToXk?method=verify&USERNAME='+str(username)+'&PASSWORD='+pwd
login = Session.get(login_url)
get_url = 'http://202.119.81.113:9080/njlgdx/kbcx/kbxx_classroom_ifr'
for zc in range(21):
	data = {'xnxqh':'2016-2017-1','skyx':'','xqid':'01','jzwid':'6','zc1':str(zc+1),'zc2':str(zc+1),'xq':'1','xq2':'7','jc1':'1','jc2':'12'}
	result = Session.post(get_url,data=data)
	PrintSQL(result,zc+1)



