#!/bin/usr/python2

#GENERAL COMMANDS FOR LINUX USER

import os
print "PRESS 0 FOR :  For MAIN MENU " #+
print "PRESS 1 FOR :  OPENING SOFTWARES"#+
print "PRESS 2 FOR :  INSTALING SOFTWARES"#+
print "PRESS 3 FOR :  CREATING NEW FOLDER" #+
print "PRESS 4 FOR :  DELEATING  FOLDER" #+
print "PRESS 5 FOR :  CREATING NEW TEXT FILES" #+
print "PRESS 6 FOR :  DELEATING TEXT FILES" #+
print "PRESS 7 FOR :  CREATING NEW USER"#+
print "PRESS 8 FOR :  ADDING PASSWARD TO THE USER "
print "PRESS 9 FOR :  DELEATING A USER"
print "PRESS 10 FOR : COMAND SHELL"
print "PRESS 11 FOR : POWER OFF THE SYSTEM"#+
print "PRESS 12 FOR : REBOOT THE SYSTEM" #+

x=raw_input('ENTER YOUR REQUIREMENTS  :    ')
if x == '00 :
	os.system('python /root/Desktop/lwp/readme.py')


if x == '0' :
	os.system('python /root/Desktop/lwp/menu.py')

if x == '1' :
		n=raw_input('ENTER THE SOFTWARE NAME')
		os.system('n')
if x == '2' :
	m=raw_input('ENTER THE SOFTWARE WHICH YOU WANT OT INSTALL     :   ')
	os.system('yum  ' + m)
if x == '3' : 
	u=raw_input('enter dir name')

 	os.system('mkdir '+ u)
if x == '4' :
	u=raw_input('enter dir name')
	
 	os.system('rmdir '+ u)
if x == '5' :
	g=raw_input('enter file name')
 	os.system('gedit ' + g)
if x == '6' :
	g=raw_input('enter file name')
        os.system('gedit ' + g)
if x == '7' :
	g=raw_input('enter the user name   :   ')
	os.system('useradd ' + g)
if x == '11' :
	os.system('poweroff')
if x == '12' :
	os.system('reboot')



else:
	print "TRY AGAIN"



