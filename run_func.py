#!/usr/bin/env python

#simple function to execute a command using a subprocess
import subprocess
import getpass

def run_me(cmd):
   p1 = subprocess.Popen(cmd)
   (result,err) = p1.communicate()

def run_as_root(cmd):
   user = getpass.getuser()
   print "will run",cmd,"as root..."
   #password = getpass.getpass("pass:")
   p1 = subprocess.Popen(['sudo'] + cmd)
   (result,err) = p1.communicate()

run_as_root(['cat','/etc/passwd'])
