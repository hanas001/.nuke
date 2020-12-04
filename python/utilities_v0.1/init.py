#nuke.pluginAddPath("renderFinished")
nuke.pluginAddPath("readWrite")         #makes read out of write
nuke.pluginAddPath("revealInFinder")    #shows in finder
nuke.pluginAddPath("collapseAll")       #collapses all open windows in node graph
nuke.pluginAddPath("rotoBezier")        #sets bounding box of rotos & beziers to "no clip"
nuke.pluginAddPath("contactSheetAll")   #gethers all read nodes of the project and makes tiled board
nuke.pluginAddPath("disableErrors")     #if the node doesnt have some channel - disables it
nuke.pluginAddPath("leo_mask")          #adds channel to maskChannelInput of any node
nuke.pluginAddPath("masksAll")          #finds and collects all alpha channels to one
#nuke.pluginAddPath("highestVersion")   #makes the version newes that is available