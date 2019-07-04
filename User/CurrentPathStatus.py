
# import sublime, sublime_plugin, os

# class ShowFilenameInStatus(sublime_plugin.EventListener):
# 	def on_activated_async(self, view):
# 	    filename = os.path.split(view.file_name())[1]
#  		path = os.path.dirname(view.file_name())
# 	    if filename is None:
# 	        view.erase_status('_filename')
# 	    else:
# 	        view.set_status('‘encoding’', "file:     " path + filename)
	  #       view.set_status(‘encoding’, view.encoding())
			# view.set_status(‘currentPath’, view.file_name())
			# view.set_status(‘lineending’, view.line_endings())
			# view.set_status(‘readonly’, Status)

import sublime, sublime_plugin, os

class ShowFilenameInStatus(sublime_plugin.EventListener):
	def on_activated_async(self, view):
	    filename = os.path.split(view.file_name())[1]
	    path = os.path.dirname(view.file_name())
	    if filename is None:
	        view.erase_status('_filename')
	    else:
	        # view.set_status('_filename', "           Path: " + path+"         FileName:  "+filename+"   ")
	        view.set_status('_filename', "Path: " + path+"\\"+filename)

# 	        import sublime_plugin

# class StatusBar(sublime_plugin.EventListener):
# def on_activated_async(self, view):
# if view.is_read_only():
# Status = “ReadOnly”
# else:
# Status = “Full”
# view.set_status(‘encoding’, view.encoding())
# view.set_status(‘currentPath’, view.file_name())
# view.set_status(‘lineending’, view.line_endings())
# view.set_status(‘readonly’, Status)


# import sublime
# import sublime_plugin

# import os
# import subprocess

# try:
#   from StatusMessage import status_message
# except ImportError as error:
#   sublime.error_message("Dependency import failed; please read readme for " +
#    "ShellStatus plugin for installation instructions; to disable this " +
#    "message remove this plugin; message: " + str(error))
#   raise error

# class ShellStatusListener(sublime_plugin.EventListener):
#   def on_activated_async(self, view):
#     settings = sublime.load_settings('ShellStatus.sublime-settings')
#     command = view.settings().get('status_command') or settings.get('command')

#     if command == 'DEFAULT':
#       command = sublime.packages_path() + '/ShellStatus/sublime-status'

#     if command == None:
#       return

#     args = [command]
#     if view.file_name() != None:
#       path = os.path.dirname(view.file_name())
#       args.append(view.file_name())
#     else:
#       path = '/'

#     process = subprocess.Popen(args, stdout=subprocess.PIPE,
#       stderr=subprocess.PIPE, cwd=path)

#     status, err = process.communicate()
#     status = status.decode('UTF-8').strip()
#     # __ is for very first position
#     status_message.set(view, '__', status)
