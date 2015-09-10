from flask import Flask
from flask_restful import Resource, Api

import math
import psutil

class getMemory(Resource):
	def get(self):
		mem=psutil.virtual_memory()
		return {'totalMemory' : mem.total, 'availableMemory' : mem.available, 'freeMemory' : mem.free}


class getCPU(Resource):
	def get(self):
		cpu=psutil.cpu_times()
		return {'cpuuser' : cpu.user, 'cpusystem' : cpu.system, 'cpuidle' : cpu.idle, 'cpuiowait' : cpu.iowait}


class getCPUPercent(Resource):
	def get(self):
		cpu=psutil.cpu_times_percent(interval=1,percpu=False)
		return {'cpuuser' : cpu.user, 'cpusystem' : cpu.system, 'cpuidle' : cpu.idle, 'cpuiowait' : cpu.iowait}


class getStorage(Resource):
	def get(self):
		storage=psutil.disk_usage('/')
		return {'roottotal' : storage.total, 'rootused' : storage.used, 'rootfree' : storage.free, 'rootfreepercent' : storage.percent }


class getUsers(Resource):
	def get(self):
		users=psutil.users()
		for u in users:
			return {'username' : u.name, 'userterminal' : u.terminal, 'userhost' : u.host}
			


class frontPage(Resource):
	def get(self):
		return {'Hello' : 'World'}
		
