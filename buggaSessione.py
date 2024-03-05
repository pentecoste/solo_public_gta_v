import psutil
import os
from time import sleep

PROCNAME = "GTA5.exe"
pid = -1

for proc in psutil.process_iter():
	try:
		if proc.name() == PROCNAME:
			pid = proc.pid
	except:
		pass
		
if pid == -1:
	print("Error: can't find GTA5.exe. Are you sure it is running?")
	quit()

proc = psutil.Process(pid)
proc.suspend()

sleep(10)

proc.resume()