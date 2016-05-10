import datetime
import random

data1 = '<?xml version="1.0" encoding="UTF-8" ?>\
<deposits>\
<deposit venue="" transaction="transactionid" amount="500" timestamp="timestampvalue"/>\
</deposits>'

data2 = '<?xml version="1.0" encoding="UTF-8" ?>\
<deposits>\
<deposit venue="aaaaaa111111" transaction="transactionid" amount="500" timestamp="timestampvalue"/>\
</deposits>'

def run(http, config):
  h = {'Content-Type' : 'application/xml'}
  global data1, data2
##TC venue == null
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
  if d.find('INVALID_VENUE'):
    res = 'Pass'
  else:
    res = 'Fail'
    comment = 'Failed venue id == null/'
##TC venue non-existing
  timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
  data2 = data2.replace('timestampvalue',timestamp)
  transid = timestamp + str(random.randint(10000, 99999))
  data2 = data2.replace('transactionid',transid)
  http.request("POST", config['d-url'], data2, h)
  resp = http.getresponse()
  d = resp.read()
  print resp.status, d
  if d.find('INVALID_VENUE'):
    if res == 'Pass':
      res = 'Pass'
  else:
    res = 'Fail'
    comment = comment + 'Failed venue id is non-existing'
  return res, comment
