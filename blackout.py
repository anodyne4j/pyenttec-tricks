import pyenttec as dmx
from time import sleep

port = dmx.select_port()

port.blackout()
port.render()
port.close