import os
import datetime
import random

def getList():
  filepath = os.getcwd() + '/tclist'
  f = open(filepath)
  tclist = f.readlines()
  f.close()
  return tclist

def getTimestamp():
  return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

def getTransId():
  return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ') + str(random.randint(10000, 99999))
