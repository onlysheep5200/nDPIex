import random
ips = ['10.0.2.15','10.0.2.16','10.0.2.17','10.0.2.18']

from_ip = '10.0.2.15'
to_ip = '10.0.3.18'

route1 = 's1->s3->s4'
route2 = 's1->s2->s4'

flows = []
for i in xrange(10) :
	route = route1
	if random.randint(0,10)>7:
		route = route2
	flow = 'flow from %s:%d to %s:%d route is %s'%(from_ip,random.randint(1024,65535),to_ip,random.randint(1024,65535),route)
	if route == route1 : 
		flows.append(flow)
	print flow

for flow in flows[0:2] : 
	print "%s change to %s"%(flow,route2)


for i in xrange(5) :
	route = route1
	if random.randint(0,10)>7:
		route = route2
	flow = 'flow from %s:%d to %s:%d route is %s'%(from_ip,random.randint(1024,65535),to_ip,random.randint(1024,65535),route)
	if route == route1 : 
		flows.append(flow)
	print flow



