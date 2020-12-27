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


from subprocess import Popen
import os
import getpass

__version__='0.0'

class CustomTextFile(object):


	def Merge(self,output,list_of_texts):
		'''Merge a list of textfiles in to an output file'''

		import fileinput
		
		with open(output, 'w') as outfile:
			for fname in list_of_texts:
				with open(fname) as infile:
					for line in infile:
						outfile.write(line)



	def GetNumberOfLines(self,file):
		'''Return the number of lines in a file. If it 
			doesn't exists it returns -1'''
		
		if os.path.exists(file):	
			with open(file) as f:
				return sum(1 for _ in f)
		else:
			return -1
			
	def HasString(self,string,text):
		'''If the string exist in the text return True,
			else return False'''
		
		for line in open(text):
			if string in line:
				return True
		return False
	
	def CurrentUserCanWrite(self,path):
		'''If the current user has permission on the path returns True, else returns False'''
		
		result=os.popen("if [ -w '"+path+"' ] ;then echo 'True' ;else echo 'False';  fi")
		result=str(result.read())
		result=result.strip()
		
		if result=="True" or getpass.getuser()=='root':																			
			return True
		else:
			return False
