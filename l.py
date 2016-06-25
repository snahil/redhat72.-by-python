#!/bin/usr/python2
import os
print "Enter user name :   "
u=raw_input()
print " Enter passward for the account  : "
p=raw_input() 

if u == 'root' and p == 'redhat' :
	os.system('python /root/Desktop/lwp/menu.py')
else :
 	print" NOT AUTHORISED "
