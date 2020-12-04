import nuke

def collapseOpenWindows():
    for node in nuke.allNodes():
        node.hideControlPanel()
