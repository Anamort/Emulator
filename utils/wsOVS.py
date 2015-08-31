#!/usr/bin/python
from flask import Flask
import commands
import re



#app = Flask(__name__)

#@app.route('/snmp/atp/<address>')
def getInfo(address):
    print address
    tempArray = commands.getstatusoutput('ovs-vsctl --db=tcp:%s:6640 list bridge' % address)
    regexp = re.compile('.*ip_addresses="(.*)"}', re.DOTALL)
    field = regexp.match(tempArray[1]).group(1)
    interfaces = field.split("/")
    print interfaces
    #temp =tempArray[1]
    #resultArray = temp.split('STRING:')
    #result = resultArray[1].strip()
    #return result

if __name__ == '__main__':
  getInfo("192.168.1.14")
    #app.run(host='0.0.0.0')
	#default port: 5000
	
