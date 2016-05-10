#!/usr/bin/python2.7
import os
import httplib
import sys
sys.path.append(os.getcwd())
sys.path.append(os.getcwd()+'/tc')
import conf
import importlib
import lib

config = conf.getConf()
##print config
try:
  con = httplib.HTTPConnection(config['SrvIp'], config['SrvPort'], timeout = 30)
##Open file for result
  fn = 'res' + lib.getTimestamp()
  f = open(fn, 'w')
##Read from test cases list
  tclist = lib.getList()
  for tcname in tclist:
    tcname = tcname.strip("\n")
##Execute each tc by tcname.run
    tcmod = importlib.import_module(tcname)
    res, comment = tcmod.run(con, config)
    result = '\'' + tcname + '\' result: ' + res + '. Comment: ' + comment +'.\n'
    print result
##And collect result from tcname.run
##Write result to a file
    f.write(result)

  f.close()
  con.close()
except Exception, e:
  print e
finally:
  if f:
    f.close()
  if con:
    con.close()
