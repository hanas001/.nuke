import nuke
import os
import sys
import subprocess

def add_reveal_button():
	node = nuke.thisNode()
	button_reveal = nuke.PyScript_Knob("revealInFinder", "reveal in finder", "")
	tab_custom = nuke.Tab_Knob("custom", "custom")
	node.addKnob(tab_custom)
	node.addKnob(button_reveal)
	
def reveal_in_finder():
	node = nuke.thisNode()
	knob = nuke.thisKnob()
	
	if knob.name() == "revealInFinder":
		path = os.path.dirname(node["file"].getValue())
		if os.path.isdir(path):
			open_folder(path)
		else:
			nuke.message("no such path")

def open_folder(path):

	if sys.platform == "darwin":
		subprocess.check_call(["open", path])
	if sys.platform == "linux2":
		subprocess.check_call(["gnome-open", path])
	if sys.platform == "win32":
		path = path.replace('/', os.sep)	#chenges slash to back slash in windows OS
		subprocess.check_call(["explorer", path])