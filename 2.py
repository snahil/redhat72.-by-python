#!/bin/usr/python2
# Memory management
import os

print" press 0  : For MAIN MENU "
print" press 1  : For disk manage help check"
print" press 2  : For diff hdd's in system"
print"  NOTE NEED TO SPECFY THE HDD NAME IN THE FOR THE EXECUTION OF THE COMAND 4 I.E /DEV/SDA
	


x=raw_input('ENTER YOUR REQUEST  ::   ')
 

if x == '0' :
	os.system('python /root/Desktop/lwp/menu.py')
if x == '1' :
	os.system('fdisk')
if x == '2' :
	os.system('fdisk -s')
if x == '3':
	u=raw_input('ENTER THE NAME OF THE HDD :  ')
	os.system('/dev/ ' + u)
if x == '4'
        
else :
	
	print "try again"

