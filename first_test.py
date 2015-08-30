import pyenttec as dmx
from time import sleep

port = dmx.select_port()

while True:
	port.blackout()
	port.render()
	sleep(2)

	i = 0
	while i < 24:
		b = 0
		while b <= 100:
			sleep(0.001)
			port.set_channel(i, b)
			print "set channel " + str(i) + " to " + str(b)
			port.render()
			b = b + 1
		i = i + 3

	i = 0
	while i < 24:
		sleep(0.01)
		b = 0
		while b <= 100:
			sleep(0.001)
			port.set_channel(i, (100-b))
			port.set_channel((i+1), b)
			print "set channel " + str(i) + " to " + str(100-b) + " and channel " + str(i+1) + " to " + str(b)
			port.render()
			b = b + 1
		i = i + 3


	i = 0
	while i < 24:
		sleep(0.01)
		b = 0
		while b <= 100:
			sleep(0.001)
			port.dmx_frame[(i+1)] = (100-b)
			port.dmx_frame[(i+2)] = b
			print "set channel " + str((i+1)) + " to " + str(100-b) + " and channel " + str(i+2) + " to " + str(b)
			port.render()
			b = b + 1
		i = i + 3

	sleep(2)	
