import nuke
import PySide.QtGui
import os



"""
this module contains functionality of notifying user when render is finished
It will play sound and show notification window
"""


# renderFinished settings
##############################################################################

# show_notification: if True show message "render is finished" when render is done
show_notification = True

# play_sound: if True play sound when render is done
play_sound = True

# sound_file: path to our sound file
sound_file = "{}/tada.wav".format(os.path.dirname(__file__))

##############################################################################

def notify_user():
"""
play a sound and show a notification when finished
:return: None
"""

	if play_sound:
		PySide.QtGui.play(sound_file)
	if show_notification:
		nuke.message("Finished rendering")