import nuke
import disableErrors

nuke.menu("Nuke").addCommand("PAROVOZ[leo]/Disable selected Errored nodes", "disableErrors.disableErrorsFunction()", "ctrl+r")