#!/usr/bin/env python

#simple function to execute a command using a subprocess
import subprocess
import getpass

def run_me(cmd):
   p1 = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
   (result,err) = p1.communicate()
   print result

def run_as_root(cmd):
   user = getpass.getuser()
   print "will run",cmd,"as root..."
   #password = getpass.getpass("pass:")
   p1 = subprocess.Popen(['sudo'] + cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=False)
   (result,err) = p1.communicate()

run_me(['cat','/etc/passwd'])
