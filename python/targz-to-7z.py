#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#

#  Copyright (C) 2015  Rafael Senties Martinelli
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


"""
	This script converts all the tar.gz archives of a directory to 7z
	by excluding the filetypes of "create_exclude".
	
	The directory must not have any other directory inside it before
	runing the script !
	
	The 7z package will exclude the file formats of the function
	create_exclude()
	
"""


import os

def create_exclude():
	
	with open(path+'/exclude', 'w') as f:
		f.write('''*.tar.gz
*.deb
*.ogg
*.webm	
''')

def delete_exclude():
	os.remove(path+'/exclude')
	

path=os.path.dirname(os.path.realpath(__file__))

files_to_extract=os.listdir(path)

for file in files_to_extract:
	

	name=file[:-7]
	current_files=os.listdir(path)

	if "tar.gz" in file and not os.path.exists(path+'/'+name+'7z'):
		os.system('tar xzvf "'+path+'/'+file+'"')

		new_files=os.listdir(path)
		
		for current_file in current_files:
			new_files.remove(current_file)
		
		if len(new_files) > 1:
			print "\nmore than two folders!"
			print new_files
			exit()
		elif len(new_files)==0:
			print "\n nothing has been extracted!"
			print path+'/'+file
			exit()
		elif len(new_files)==1:
			create_exclude()
			os.system("7z a -r -x@exclude '"+name+".7z' '"+path+'/'+new_files[0]+"'")
			delete_exclude()
			os.system('''rm -rf "'''+path+'/'+new_files[0]+'"')
	





