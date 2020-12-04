import nuke
import collapseAll

nuke.menu("Nuke").addCommand("PAROVOZ[leo]/Collapse All Windows", "collapseAll.collapseOpenWindows()", "A", shortcutContext=2)
