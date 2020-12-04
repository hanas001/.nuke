import nuke
import masksAll

nuke.menu("Nuke").addCommand("PAROVOZ[leo]/Find and collect all masks", "masksAll.collectAllMasks()", 'E')