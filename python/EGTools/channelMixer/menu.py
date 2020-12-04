import nuke
import channelMixer
import re

nuke.menu('Nodes').addCommand('PAROVOZ[leo]/channelMixer', 'nuke.createNode("channelMixer")')
