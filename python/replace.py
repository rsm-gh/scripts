#!/usr/bin/python3

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

import os

__version__ = '1.0'

PATH="./"
SEARCH_STRING='left-listing.css'
REPLACE_STRING='left-listing-1.css'
IGNORED_EXTESIONS=('.png','.jpeg','.jpg','.gif','.pdf','.db','.odg','.wav','.pyc','.zip','.7z','.o','.sqlite3','.sock','.log')
IGNORED_INCLUDE_STRINGS=['.git']

_ignored_files=[]
_files_to_replace=[]
_script_path=os.path.realpath(__file__)


for dirpath, _, filenames in os.walk(PATH):
       for filename in filenames:
            file_path = os.path.abspath(os.path.join(dirpath, filename))
            
            if not any(file_path.lower().endswith(extension) for extension in IGNORED_EXTESIONS) and \
               not any(include_string in file_path.lower() for include_string in IGNORED_INCLUDE_STRINGS):
            
                try:
                    with open(file_path, 'r') as f:
                        if SEARCH_STRING in f.read():
                            if not file_path == _script_path:
                                _files_to_replace.append(file_path)
        
                except:
                    _ignored_files.append(file_path)               



print("**** IGNORED FILES *******")
for filepath in _ignored_files:
    print(filepath)
    

print("\n**** FILES TO REPLACE *******")
for filepath in _files_to_replace:
    print(filepath)


if input("\n Do you want to make the replacement? (y/n)").lower().startswith("y"):
    for filepath in _files_to_replace:
        with open(filepath, 'r+') as f:
            
            content = f.read().replace(SEARCH_STRING, REPLACE_STRING)
            f.seek(0)
            f.write(content)
            f.truncate()
            
        print(filepath)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
