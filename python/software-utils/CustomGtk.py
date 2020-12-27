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

from gi.repository import Gtk

# Imports from files of Fresh Install
from Paths import *
from Messages import *

__version__='0.0'

def filter_files_including_folders(filter_info, self):
	if type(filter_info) is str:
		path=filter_info
	else:
		path=str(filter_info.filename)

	for folder in self.FoldersToReplace_List:
		if path in folder.ComputerPath():
			return False

	for file in self.FilesToReplace_List:
		if path == file.ComputerPath():
			return False

	return True

def filter_files(filter_info, self):
	if type(filter_info) is str:
		path=filter_info
	else:
		path=str(filter_info.filename)

	for file in self.FilesToReplace_List:
		if path == file.ComputerPath():
			return False
				
	return True
	
def filter_renamed_files(filter_info, self):
	if type(filter_info) is str:
		path=filter_info
	else:
		path=str(filter_info.filename)


	for file in self.FilesToRename_List:
		if path == file.ComputerPath():
			return False
				
	return True	
	
def filter_folders(self,filter_info,Data):

	if type(filter_info) is str:
		path=filter_info
	else:
		path=str(filter_info.uri)
		
	for folder in self.FoldersToReplace_List:
		if path == folder.ComputerPath():
			return False
			
	return True

'''
# There is no option to hide folders in GTK, so
# the feature must be requested before using this function.

def FILTER_folders(self):

	filter=Gtk.FileFilter()
	filter.set_name(TEXT_NON_SELECTED_FOLDERS)
	filter.add_custom(Gtk.FileFilterFlags.URI,filter_folders,None)
	self.window_choose_folder.add_filter(filter)

	filter1=Gtk.FileFilter()
	filter1.set_name(TEXT_DISPLAY_ALL)
	filter1.add_pattern("*")
	self.window_choose_folder.add_filter(filter1)
'''



def FILTER_ini(self):
	filter=Gtk.FileFilter()
	filter.set_name("Config")
	filter.add_pattern("*.ini")
	self.window_choose_file.add_filter(filter)	

def FILTER_files(self):
	filter=Gtk.FileFilter()
	filter.set_name(TEXT_NON_SELECTED_FILES_INCLUDING_FOLDERS)
	filter.add_custom(Gtk.FileFilterFlags.FILENAME, filter_files_including_folders, self)	
	self.window_choose_file.add_filter(filter)

	filter2=Gtk.FileFilter()
	filter2.set_name(TEXT_NON_SELECTED_FILES)
	filter2.add_custom(Gtk.FileFilterFlags.FILENAME, filter_files, self)
	self.window_choose_file.add_filter(filter2)

	filter3=Gtk.FileFilter()
	filter3.set_name(TEXT_DISPLAY_ALL)
	filter3.add_pattern("*")
	self.window_choose_file.add_filter(filter3)


def FILTER_files_to_rename(self):
	
	filter=Gtk.FileFilter()
	filter.set_name(TEXT_HIDE_REANAMED_FILES)
	filter.add_custom(Gtk.FileFilterFlags.FILENAME, filter_renamed_files, self)
	self.window_choose_file.add_filter(filter)

	filter1=Gtk.FileFilter()
	filter1.set_name(TEXT_DISPLAY_ALL)
	filter1.add_pattern("*")
	self.window_choose_file.add_filter(filter1)


def AskForFile(self,PARENT,MODE):

	self.window_choose_file=Gtk.FileChooserDialog(TEXT_CHOOSE_ANOTHER_FILE,PARENT,
	   Gtk.FileChooserAction.OPEN,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
	self.window_choose_file.set_default_response(Gtk.ResponseType.NONE)
	self.window_choose_file.set_icon_from_file(MAIN_ICON_SMALL)
	
	self.window_choose_file.set_transient_for(PARENT)

	self.window_choose_file.show()
	if MODE=="external_config":
		FILTER_ini(self)
	elif MODE=="rename":
		FILTER_files_to_rename(self)
	else:
		FILTER_files(self)
	
	if self.default_file_chooser_path!=None:
		self.window_choose_file.set_current_folder(self.default_file_chooser_path)
	
	
	response=self.window_choose_file.run()
	if response == Gtk.ResponseType.OK:
		file_path=self.window_choose_file.get_filename()
		self.window_choose_file.destroy()
		
		if file_path and os.path.exists(file_path):
			self.default_file_chooser_path=(os.path.dirname(file_path))
		
		return file_path
	else:
		self.window_choose_file.destroy()



def AskForFolder(self,PARENT):

	self.window_choose_folder=Gtk.FileChooserDialog(TEXT_CHOOSE_ANOTHER_FOLDER,PARENT,Gtk.FileChooserAction.SELECT_FOLDER,(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
	self.window_choose_folder.set_icon_from_file(MAIN_ICON_SMALL)

	if self.default_folder_chooser_path!=None:
		self.window_choose_folder.set_current_folder(self.default_folder_chooser_path)
	
	#FILTER_folders(self)
	
	self.window_choose_folder.show()
	response=self.window_choose_folder.run()
	if response == Gtk.ResponseType.OK:
		folder_path=self.window_choose_folder.get_filename()
		self.window_choose_folder.destroy()
		
		if folder_path and os.path.exists(folder_path):
			self.default_folder_chooser_path=os.path.dirname(folder_path)
		
		return folder_path
	else:
		self.window_choose_folder.destroy()



class CustomGtk(object):

	def info(self,PARENT,text1,text2):

		dialog=Gtk.MessageDialog(PARENT,Gtk.DialogFlags.MODAL,Gtk.MessageType.INFO,Gtk.ButtonsType.CLOSE,text1)
		dialog.set_default_response(Gtk.ResponseType.NONE)
		dialog.set_icon_from_file(MAIN_ICON_SMALL)

		#h_button_box=dialog.vbox.get_children()[1]
		#close_button=h_button_box.get_children()[0]
		#close_button.unset_flags(CAN_FOCUS)
		#print str(close_button)
		#print close_button.get_state_flags()
		#print close_button.has_default()
		#print close_button.has_focus()
		#print close_button.has_visible_focus()
		#close_button.unset_state_flags(Gtk.CAN_DEFAULT)

		if text2 != None:
			dialog.format_secondary_text(text2)
		
		response=dialog.run()
		dialog.destroy()
		


	def question(self,PARENT,text1,text2):

		dialog=Gtk.MessageDialog(PARENT,Gtk.DialogFlags.MODAL,Gtk.MessageType.QUESTION,Gtk.ButtonsType.YES_NO,text1)
		dialog.set_icon_from_file(MAIN_ICON_SMALL)
		
		if text2 != None:
			dialog.format_secondary_text(text2)
		
		response=dialog.run()
		if response == Gtk.ResponseType.YES:
			dialog.hide()
			return True
			
		elif response == Gtk.ResponseType.NO:
			dialog.hide()
			return False
			
	def retrive_combobox_value(self,widget,ENTRY):

		if ENTRY:
			tree_iter=widget.get_active_iter()
			if tree_iter != None:
				model=widget.get_model()
				row_id, item=model[tree_iter][:2]
			else:
				entry=widget.get_child()
				item=entry.get_text()
		else:
			tree_iter=widget.get_active_iter()
			if tree_iter != None:
				model=widget.get_model()
				item=model[tree_iter][1]

		return item
		
	def rgba_to_hex(self,rgba):
		red=(rgba.red * 255)
		green=(rgba.green * 255)
		blue=(rgba.blue * 255)
		return ("#%02x%02x%02x" % (red, green, blue))
		
		
	def ListStoreNbRows(self,liststore):
		i=0
		for row in liststore:
			i+=1
			
		return i
