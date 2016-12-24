#!/usr/bin/env python

#simple function to execute a command using a subprocess
import subprocess

def run_me(cmd):
   p1 = subprocess.Popen(cmd)
   (result,err) = p1.communicate()

run_me("ls")
