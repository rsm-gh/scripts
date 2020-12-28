#! /usr/bin/python3
#* coding:utf8 *
   
#
# Qt5 code snippet - exemple of a loading window
#
# Written in 2019 by Rafael SENTIES MARTINELLI
#
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain 
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along with
# this software. If not, see <http://creativecommons.org/publicdomain/zero/1.0/>. 
#

import sys
import os

project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, project_path)

from main_window.MainWindow import main

main()