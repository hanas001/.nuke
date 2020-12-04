import nuke
import rotoBezier

nuke.menu("Nuke").addCommand("PAROVOZ[leo]/Roto or Bezier Bounding Box", "rotoBezier.noBoundingBox()", shortcutContext=2)
