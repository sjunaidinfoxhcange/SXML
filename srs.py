import sublime
import sublime_plugin
import sublime_api

import sys

import sublime_api
from collections import namedtuple
from datetime import datetime
import functools
import fnmatch
from itertools import groupby
import logging
from os import path, walk
import re
import threading

import sublime
import sublime_plugin






class ToggleReadonlyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        
            self.view.set_read_only(True)
            self.view.set_status('toggle_readonly', '')
            sublime.status_message("Buffer " + str(self.view.file_name()) + " is writeable again.")





class ToggleReadonlyListener(sublime_plugin.EventListener):
    @staticmethod
    def check_readonly(view):
        if view.is_read_only():
            view.set_status('toggle_readonly', 'Readonly')
        else:
            view.set_status('toggle_readonly', '')

    def on_activated(self, view):
        ToggleReadonlyListener.check_readonly(view)




class OpenFileonlyCommand(sublime_plugin.TextCommand):



 def run(self, edit, **args ):
        old_selections = args['fname']

        #print(self.view.window().active_view().file_name())



        #self.window.open_file(self,old_selections)
      #  return View(sublime_api.window_open_file(self.window_id, fname, flags, group))

        #window_id =  self.view.id()
        #print(window_id)
        print( str( old_selections ) )

        #self.window().active_view().new_file(old_selections)
        self.view.window().open_file(old_selections)
        self.view.set_read_only(True)

       # self.view.window().find_open_file(args['ff']).set_read_only(True)
        
       
        
        
        

        #return View( sublime_api.window_open_file(window_id, old_selections, flags, group))


        


class AssistantCommand( sublime_plugin.TextCommand ):
    def run( self, edit, old_selections ):
        print( str( old_selections ) )


class AssistantCommand( sublime_plugin.TextCommand ):

    def run( self, edit, *old_selections ):
        print( str( old_selections ) )

class AssistantCommand( sublime_plugin.TextCommand ):

    def run( self, edit, **kargs ):
        old_selections = kargs["args"]
        print( str( old_selections ) )


      ## def open_fileonly(self,fname,edit):
        """
        valid bits for flags are:
        ENCODED_POSITION: fname name may have :row:col or :row suffix
        TRASIENT: don't add the file to the list of open buffers
        FORCE_GROUP: don't select the file if it's opened in a different group
        """
      ##  return View(sublime_api.window_open_file(self.window_id, fname, 0, -1))

###
