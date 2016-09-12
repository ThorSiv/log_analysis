#!/usr/bin/python
#-*- coding: UTF-8 -*-
import re,os,time,commands
def catch():
	f = open("/opt/bitcoin/bitcoindata/debug.log")
	f.seek(1,2)
	line = f.readline()

	while True:
        	pattern = re.compile(r'(.*) Update.*best=(.*)  height=(.*)  log.* pro')
        	#pattern = re.compile(r'best=(.*)  height=(.*)  log.*  date=(.*) pro')

        	match = pattern.search(line)
        	if match:
               		best = match.group(2)
                	height = match.group(3)
                	date = match.group(1)
                #print best
                #print height
                #print date
			#curl -d "blkhash=" -d "height=" -d "date=" http://101.200.135.109:8080/bitcoind/monitor/broadcast.htm?
			status = 1
			while status != 0:
				(status, output) = commands.getstatusoutput("curl --connect-timeout 30 -d 'blkhash="+best+"' -d 'height="+height+"' -d 'date="+date+"' http://101.200.135.109:8080/bitcoind/monitor/broadcast.htm?")
			                                                         		
			#os.system("curl --connect-timeout 30 -d 'blkhash="+best+"' -d 'height="+height+"' -d 'date="+date+"' http://101.200.135.109:8080/bitcoind/monitor/broadcast.htm?")
                	#os.system("curl http://101.200.135.109:8080/bitcoind/monitor/broadcast.htm?blkhash="+best+"\&height="+height+"\&date="+date+" 1>/dev/null 2>&1")
                	#os.system("curl http://101.200.135.109:8080/bitcoind/monitor/broadcast.htm?blkhash="+best+"\&height="+height+"\&date="+date+" 1>/dev/null 2>&1")
                	os.system("echo 'blkhash="+best+"height="+height+"date="+date+"' >> remote.log")
        	line = f.readline()
		i = 1
        	while  line == "":
                	time.sleep(2)
                	line = f.readline()
			if i > 40:
				f.close()
				catch()
			i += 1
catch()


