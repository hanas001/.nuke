import nuke


def leo_tig_mask ():
	pan = nuke.Panel('Leo and Tig: add mask')
	textinput = 'example: other.mask_'
	pan.addMultilineTextInput('compose_mask', textinput)
	pan.show()
	maskvalue = pan.value('compose_mask')
	nuke.selectedNode().knob('mask').setValue( maskvalue ) 