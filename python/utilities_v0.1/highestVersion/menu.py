import nuke
import highestVersion

nuke.menu("Nuke").addCommand("PAROVOZ[leo]/Make the newest version", "highestVersion.highestVersion()", "H", shortcutContext=2)
