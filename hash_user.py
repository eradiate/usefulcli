#!/usr/bin/env python

#hashing passwd and shadow for fun
#taking the passwd file and hash the user with the shadow and group

up = '/etc/passwd'
sh = '/etc/shadow'
gr = '/etc/group'

users = {}

userp = open(up,'r')
allusers = userp.readlines()

for au in allusers:
   users[au.split(':')[0]] = {}
   users[au.split(':')[0]]['shell']=au.split(':')[6]



for (k,v) in users.iteritems():
  print k,v

