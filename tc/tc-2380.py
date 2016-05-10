import datetime
import random

data1 = '<?xml version="1.0" encoding="UTF-8" ?>\
<deposits>\
<deposit venue="1" transaction="transactionid" amount="500" timestamp="timestampvalue"/>\
</deposits>'

def run(http, config):
  h = {'Content-Type' : 'application/xml'}
  global data1
  timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
  data1 = data1.replace('timestampvalue',timestamp)
  transid = timestamp + str(random.randint(10000, 99999))
  data1 = data1.replace('transactionid',transid)
  http.request("POST", config['d-url'], data1, h)
  resp = http.getresponse()
  d = resp.read()
  res = ''
  comment = ''
  print resp.status, d
  if resp.status == 204:
    res = 'Pass'
  else:
    res = 'Fail'
    comment = d
  return res, comment
