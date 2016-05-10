#!/usr/bin/python2.7
import json
import os

def getConf():
  filepath = os.getcwd() + '/conf/test.conf'
  f = open(filepath)
  confdata = f.read()
  f.close()
  c = json.loads(confdata)
  return c
