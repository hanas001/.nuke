import nuke
import contactSheetAll

nuke.menu("Nuke").addCommand("PAROVOZ[leo]/Contact Sheet All", "contactSheetAll.contactSheetFunction()", "shift+c")