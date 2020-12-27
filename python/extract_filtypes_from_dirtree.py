#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#

#  Copyright (C) 2016  Rafael Senties Martinelli
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
    Traverse a dirtree and copy all the files matching the extensions
"""


PATH='./rec'
DESTINATION='./bk'
EXTENSIONS=('.ods','.odt','.pdf','.doc')



import os
from shutil import copy, rmtree

rmtree(DESTINATION)
os.mkdir(DESTINATION)


for root, dirs, files in os.walk(PATH):
    for file in files:
        absolute_path=os.path.join(root,file)
        if any(absolute_path.lower().endswith(extension) for extension in EXTENSIONS):

            print(absolute_path)
            
            copy(absolute_path, '{}/{}'.format(DESTINATION, os.path.basename(absolute_path)))

            
