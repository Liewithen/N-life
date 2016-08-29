#!/usr/bin/env python
# coding:utf-8

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()


import django

if django.VERSION >= (1, 7):
	django.setup()

def main():
	from search.models import SAOW1,SAOW2,SAOW3,SAOW4,SAOW5,SAOW6,SAOW7,SAOW8,SAOW9,SAOW10,SAOW11,SAOW12,SAOW13,SAOW14,SAOW15,SAOW16,SAOW17,SAOW18,SAOW19,SAOW20,SAOW21
	f = open("Room_Info/1.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW1.objects.bulk_create(RoomList)
	f = open("Room_Info/2.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW2.objects.bulk_create(RoomList)
	f = open("Room_Info/3.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW3.objects.bulk_create(RoomList)
	f = open("Room_Info/4.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW4.objects.bulk_create(RoomList)
	f = open("Room_Info/5.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW5.objects.bulk_create(RoomList)
	f = open("Room_Info/6.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW6.objects.bulk_create(RoomList)
	f = open("Room_Info/7.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW7.objects.bulk_create(RoomList)
	f = open("Room_Info/8.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW8.objects.bulk_create(RoomList)
	f = open("Room_Info/9.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW9.objects.bulk_create(RoomList)
	f = open("Room_Info/10.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW10.objects.bulk_create(RoomList)
	f = open("Room_Info/11.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW11.objects.bulk_create(RoomList)
	f = open("Room_Info/12.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW12.objects.bulk_create(RoomList)
	f = open("Room_Info/13.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW13.objects.bulk_create(RoomList)
	f = open("Room_Info/14.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW14.objects.bulk_create(RoomList)
	f = open("Room_Info/15.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW15.objects.bulk_create(RoomList)
	f = open("Room_Info/16.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW16.objects.bulk_create(RoomList)
	f = open("Room_Info/17.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW17.objects.bulk_create(RoomList)
	f = open("Room_Info/18.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW18.objects.bulk_create(RoomList)
	f = open("Room_Info/19.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW19.objects.bulk_create(RoomList)
	f = open("Room_Info/20.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW20.objects.bulk_create(RoomList)
	f = open("Room_Info/21.txt")
	RoomList = []
	for line in f:
		parts = line.split(', ')
		RoomList.append(SAOW1(roomid=parts[0],timeOfDay=int(parts[1]),building=int(parts[2]),oneIsAVL=int(parts[3]),twoIsAVL=int(parts[4]),threeIsAVL=int(parts[5]),fourIsAVL=int(parts[6]),fiveIsAVL=int(parts[7])))
	f.close()
	SAOW21.objects.bulk_create(RoomList)
if __name__ == "__main__":
	main()
	print ('Data Insert Successfully !')