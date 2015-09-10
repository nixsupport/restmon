from flask import Flask
from flask_restful import Resource, Api
#import platform
from subprocess import Popen,PIPE

'''
class getPlatform(Resource):
	def get(self):
		pp=platform.uname()
		return {'operatingsystem' : pp[0], 'kernelversion' : pp[2], 'architecture' : pp[-1]}
'''

class getPlatform(Resource):
	def get(self):
		kernel=Popen(['uname','-r'],stdout=PIPE).communicate()[0].rstrip('\n')
		hostname=Popen(['uname','-n'],stdout=PIPE).communicate()[0].rstrip('\n')
		architecture=Popen(['uname','-m'],stdout=PIPE).communicate()[0].rstrip('\n')
		os=Popen(['uname','-o'],stdout=PIPE).communicate()[0].rstrip('\n')
		return {'kernelversion' : kernel, 'operatingsystem' : os,'hostname' : hostname, 'architecture' : architecture}