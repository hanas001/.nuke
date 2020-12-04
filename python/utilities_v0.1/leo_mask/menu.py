import nuke
import leo_mask

nuke.menu("Nuke").addCommand("PAROVOZ[leo]/Mask_leo", "leo_mask.leo_tig_mask()", "F10" )