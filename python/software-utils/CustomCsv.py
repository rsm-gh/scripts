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

import csv
import os

__version__='0.0'

class CustomCsv(object):

	def AlphOrganiseFile(self,list_path):
		'''Alphabetically organize a Csv file
			with out modifying the first line'''

		alf_list,start_list=[],[]
		with open(list_path, 'r') as f:
			program_list=csv.reader(f,delimiter='|')
		
			i=0
			for row in program_list:
				if i>0:
					alf_list.append(row)
				else:
					start_list.append(row)
					i+=1
			
			alf_list.sort()
			alf_list=start_list+alf_list
			
		os.remove(list_path)
		
		with open(list_path, "ab") as f:
			for row in alf_list:
				csv_list=csv.writer(f, delimiter='|')
				csv_list.writerow(row)
				
	def AddRow(self,csv_path,*args):
		with open(csv_path, "ab") as f:
			csv_list=csv.writer(f,delimiter='|')
			csv_list.writerow(args)
			
	def IncrementNumberOfColumn(self,list_path,column):
	
		new_value=0
		if not os.path.exists(list_path):
			return 0
		else:
			with open(list_path, 'r') as f:
				rows=csv.reader(f, delimiter="|")
				for row in rows:
					try:
						if row[column] > id:
							new_value=row[column]+1
					except:
						print "CustomCsv.py: IncrementNumberOfColumn: Corrupted row"
				
			return str(new_value)
			
			
	def ExistsInColumn(self,list_path,column,item_to_compare):
	
		if not os.path.exists(list_path):
			return False
		else:
			with open(list_path, 'r') as f:
				list=csv.reader(f,delimiter='|')
						
				for row in list:
					previous_items=row[column]
					if item_to_compare == previous_items:
						return True
				
				return False
				
	def CreateListFromColumn(self,list_path,column):
	
		if not os.path.exists(list_path):
			return []
		else:
			local_list=[]
			with open(list_path, 'r') as f:
				list=csv.reader(f,delimiter='|')
				next(f)
				for row in list :
					local_list.append(row[column])

			return local_list
