import logging  
import psutil
import os
import time
import argparse
import tkMessageBox
import pygal

def parse_args():
	parser = argparse.ArgumentParser(description='log for streaming')
	parser.add_argument("--t",dest='strNumber',type=int,help="choose the time",default=5)
	parser.add_argument("--n",dest='logName',type=str,help="choose the log file name",default="log")
	parser.add_argument("--exe",dest='processName',type=str,help="choose the svg file name",default="chrome.exe")

	args = parser.parse_args()
	return args


def net_io(timeInterval):

	r1 = psutil.net_io_counters().bytes_recv
	s1 = psutil.net_io_counters().bytes_sent
	time.sleep(timeInterval)
	r2 = psutil.net_io_counters().bytes_recv
	s2 = psutil.net_io_counters().bytes_sent

	y1 = r2 - r1
	y2 = s2 - s1

	recv = y1 / timeInterval
	sent = y2 / timeInterval
	return (recv/1024,sent/1024)

def get_cpu_percentage(processName):
	pidList = psutil.pids()
	for eachPid in pidList:
		try:
			specificProcess = psutil.Process(eachPid)

		except psutil.NoSuchProcess:
			pass

	else:
		processName = specificProcess.name()

		if(processName == processName):
			processPID = specificProcess.pid
	return psutil.Process(processPID).cpu_percent()