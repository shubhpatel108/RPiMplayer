import os
import time

def child():
	command = "mplayer -ao alsa -quiet -playlist playlist.m3u -slave -input file=/tmp/pipe"
	os.system(command)
	os._exit(0)  

def parent():
	newpid = os.fork()
	if newpid == 0:
		child()
	else:
		while True:
			cmd = raw_input()
			exe_cmd = "echo " + cmd + " > /tmp/pipe"
			os.system(exe_cmd)

file_name = raw_input("Enter path and name of the file to play: ")
parent()
