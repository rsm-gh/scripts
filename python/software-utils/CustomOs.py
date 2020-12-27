#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

#  Copyright (C) 2014  Rafael Senties Martinelli
#
#  This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License 3 as published by
#   the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software Foundation,
#   Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA.

import psutil, shutil, os, datetime, pwd, sys
from datetime import datetime
from inspect import currentframe, getframeinfo

## Imports from Fresh Install Files
from Messages import *
from Paths import *

__version__='0.0'

class CustomOs(object):

	def KillChildTree(self):
		'''Kill the childs of the main process'''
		 
		pid=os.getpid()
		parent=psutil.Process(pid)
		for child in parent.get_children(recursive=True):
			try:
				child.kill()
			except Exception,e: 
				frameinfo = getframeinfo(currentframe())
				print frameinfo.filename, frameinfo.lineno
				print str(e)
				
				
	def NameExistsInFolder(self,folder,name):
		'''If a name alredy exist in a folder returns True if not False'''
		
		for filename in os.listdir(folder):
			if name==filename:
				return True
		return False
		
	def GetOwner(self,path):
		if os.path.exists(path):
			st=os.stat(path)
			owner_name=pwd.getpwuid(st.st_uid).pw_name
		else:
			owner_name="None"
		
		return owner_name
		
	def GetDateTime(self):
		now=datetime.now()
		return now.strftime("%Y-%m-%d %H:%M:%S")
		
	def MakeTreeOfDirs(self,path):
		if not os.path.exists(path):
			os.makedirs(path)
		
	def GetDifferenceDateTimeAsString(self,time_to_check):

		time=self.GetDateTime()
		time=datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
		old_time=datetime.strptime(time_to_check, '%Y-%m-%d %H:%M:%S')
		delta=time-old_time
		delta=delta.days*24*60*60+delta.seconds
		
		second=1
		minut=60
		hour=minut*60
		day=hour*24
		month=day*30
		year=day*365
		
		if delta <= minut:
			if delta==1:
				difference=" %d %s " %(delta,TEXT_SECOND)
			else: 
				difference=" %d %ss " %(delta,TEXT_SECOND)
		else:
			if delta <= hour:
				AA,BB=minut,second
				CC,DD=TEXT_MINUT,TEXT_SECOND
			elif delta <= day:
				AA,BB=hour,minut
				CC,DD=TEXT_HOUR,TEXT_MINUT
			elif delta <= month:
				AA,BB=day,hour
				CC,DD=TEXT_DAY,TEXT_HOUR
			elif delta <= year:
				AA,BB=month,day
				CC,DD=TEXT_MONTH,TEXT_DAY
			
			delta1=delta/AA
			delta1=int(round(delta1))
			delta2=(delta%AA)/BB
			delta2=int(round(delta2))
			if delta1==1 and delta2==0:
				difference=" %d %s " %(delta1,CC)
			elif delta1==1 and delta2==1:
				difference=" %d %s and %d %s " %(delta1,CC,delta2,DD)
			elif delta1==1 and delta2>0:
				difference=" %d %s and %d %ss " %(delta1,CC,delta2,DD)
			elif delta1>1 and delta2==0:
				difference=" %d %ss " %(delta1,CC)
			elif delta1>1 and delta2==1:
				difference=" %d %ss and %d %s " %(delta1,CC,delta2,DD)
			else:
				difference=" %d %ss and %d %ss " %(delta1,CC,delta2,DD)

		return DIALOG_LAST_ACTUALIZATION+" "+difference
		
	def GetPathSize_GB(self,path):
		if os.path.exists(path):
			path_size=0
			if os.path.isdir(path):
				for dirpath, dirnames, filenames in os.walk(path):
					for f in filenames:
						fp=os.path.join(dirpath, f)
						if os.path.exists(fp):
							path_size += os.stat(fp).st_size

				path_size=path_size/(1024*1024.0*1024)
			else:
				path_size=os.path.getsize(path)/(1024*1014.0*1024)

			return path_size
		else:
			return 0.0
			
			
	def GetPathSize_MB(self,path):
		
		if os.path.exists(path):
			path_size=0
			if os.path.isdir(path):
				for dirpath, dirnames, filenames in os.walk(path):
					for f in filenames:
						fp=os.path.join(dirpath, f)
						if os.path.exists(fp):
							path_size += os.stat(fp).st_size

				path_size=path_size/(1024*1024.0)
			else:
				path_size=os.path.getsize(path)/(1024*1014.0)

			return path_size
		else:
			return 0.0
			
	def GetPathSize_KB(self,path):
		
		if os.path.exists(path):
			path_size=0
			if os.path.isdir(path):
				for dirpath, dirnames, filenames in os.walk(path):
					for f in filenames:
						fp=os.path.join(dirpath, f)
						if os.path.exists(fp):
							path_size += os.stat(fp).st_size

				path_size=path_size/(1024.0)
			else:
				path_size=os.path.getsize(path)/(1014.0)

			return path_size
		else:
			return 0.0
			
	def ModifiedDate_Char(self,path):
		if os.path.exists(path):
			seconds = os.path.getmtime(path)
			return str(datetime.fromtimestamp(seconds))
		else:
			return "None"
			
			
	def DeleteFromDisk(self,path):
		if os.path.exists(path):
			if os.path.isdir(path):
				shutil.rmtree(path)
			else:
				os.remove(path)
			
			
			
			
