import nuke
import readWrite

nuke.menu("Nuke").addCommand("PAROVOZ[leo]/Create read from write", "readWrite.create_read_from_write()", "alt+j")