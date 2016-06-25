#!/bin/usr/python2

# select your wish to excess 
import os



print" press 1  : For general redhat commands"   #+
print" press 2  : Memory management"#+
print" press 3  : Creating repos"#+
print" press 4  : for instaling/updating software/services"#+
print" press 5  : For user management"#+
print" press 6  : Server Menu"#+
print" press 7  : Networking menu"#+
print" press 8  : Database"#+
print" press 9  : logs"#+
print" press 10 : All "#+

print" NOTE 1 :- CTL+C FOR TAKING EXIT FORM CODE"
print" NOTE 2 :- CLEAR FOR CLEARING THE SCREEN"
print" NOTE 3 :- FOR NEW LIST ,AND OTHER USES PRESS 10"


x=raw_input('ENTER YOUR REQUEST  :    ')

if x == '0' :
	os.system('python /root/Desktop/lwp/menu.py')

if x == '1' :
	os.system('python /root/Desktop/lwp/1.py')
if x == '2' :
	os.system('python /root/Desktop/lwp/2.py')
if x == '3' :
	os.system('python /root/Desktop/lwp/3.py')
if x == '4' :
	os.system('python /root/Desktop/lwp/4.py')
if x == '5' :
	os.system('python /root/Desktop/lwp/5.py')
if x == '6' :
	os.system('python /root/Desktop/lwp/6.py')
if x == '7' :
	os.system('python /root/Desktop/lwp/7.py')
if x == '8' :
	os.system('python /root/Desktop/lwp/8.py')
if x == '9' :
	os.system('python /root/Desktop/lwp/9.py')
if x == '10' :
	os.system('python /root/Desktop/lwp/10.py')

else:
	print "TRY AGAIN"




