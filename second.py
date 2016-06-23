#!/usr/bin/python

import os
print "understanding linux"
print "press1= to openfirefox"
print "press2= to power off"
print "press3= to createdir"
print "press4= to deleadir"
print "press5= to clear terminal"
print "press6= to terminate program"


x=raw_input()

if x == '1' :

 os.system('firefox')

if x == '2' :
 os.system('power off')
if x == '3' :
 u=raw_input('enter dir name')

 os.system('mkdir '+ u)

if x == '4' :
 g=raw_input('enter file name')
 os.system('gedit ' + g)



if x == '5':
 os.system('clear')

if x == '6':
 os.system('exit')

else : print "check again"
