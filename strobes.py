import pyenttec as dmx
from time import sleep

port = dmx.select_port()

i = 0
while i < 28:
	port.dmx_frame[i] = 255
	i = i + 1

port.render()


# port.blackout()
# port.render()
# port.close