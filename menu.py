###### This is where you put your graphic user interface (GUI) customisations ######



### import Python scripts and/or Python Modules - i.e.:    import myPythonScript
import nuke


### add format resolutions presets - i.e.:    nuke.addFormat ('1920 797 0 0 1920 797 1.0 FullHD_Widescreen')
nuke.addFormat ('1920 797 0 0 1920 797 1.0 FullHD Widescreen')


### add LUT to the Root - i.e.:    nuke.root().knob('luts').addCurve('nameOfTheLUT', 'formula')    # sLOG formula example: '{pow(10.0, ((t - 0.616596 - 0.03) /0.432699)) - 0.037584}'
nuke.root().knob('luts').addCurve('TestLUT', '{pow(10.0, ((t - 0.616596 - 0.03) /0.432699)) - 0.037584}')


### customise menu items from Nodes toolbar - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').addCommand('Channel/Shuffle', 'nuke.createNode("Shuffle")', 'j', icon='Shuffle.png')
### set hotkey for an existing menu item - i.e. Shuffle hotkey 'J':    nuke.menu('Nodes').findItem('Channel').findItem('Shuffle').setShortcut('j')
#nuke.menu('Nodes').findItem('Channel').findItem('Shuffle').setShortcut('h')


#creates framehold that defaults to current frame
nuke.menu('Nodes').addCommand("Time/FrameHold", "nuke.createNode('FrameHold')['first_frame'].setValue( nuke.frame() )")


### customise node default value - i.e.:    nuke.knobDefault('myNode.myKnob', 'myDefaultValue' )
nuke.knobDefault('Blur.channels', 'alpha')
nuke.knobDefault('Blur.crop', 'false')
nuke.knobDefault('Blur.size', '1.0')

nuke.knobDefault('Bezier.output', 'alpha')
nuke.knobDefault('Bezier.size', '1.0')
nuke.knobDefault('Bezier.cliptype', 'no clip')
nuke.knobDefault('Bezier.shape', 'false')

nuke.knobDefault('Roto.cliptype', 'no clip')

nuke.knobDefault('Ramp.output', 'alpha')
nuke.knobDefault('Ramp.cliptype', 'no clip')

nuke.knobDefault('FilterErode.channels', 'alpha')
nuke.knobDefault('FilterErode.size', '-1')

nuke.knobDefault('Noise.output', 'alpha')
nuke.knobDefault('Noise.cliptype', 'no clip')

nuke.knobDefault('prvz_dailies.toshtgn', 'true')

nuke.knobDefault('Invert.channels', 'alpha')

nuke.knobDefault('Remove.operation', 'keep')
nuke.knobDefault('Remove.channels', 'rgba')

nuke.knobDefault('Merge2.also_merge', 'all')

nuke.knobDefault('xyzKey_v01.in_1', 'position')
nuke.knobDefault('xyzKey_v01.s_k', 'true')

nuke.knobDefault ( 'ContactSheet.rows' , '1' )
nuke.knobDefault ( 'ContactSheet.columns' , '2' )
nuke.knobDefault('ContactSheet.width', 'root.width()*columns')
nuke.knobDefault('ContactSheet.height', 'root.height()*rows')


### add menu item to existing Nuke menu - i.e.:    nodeMenu = nuke.menu('Nuke').findItem('Edit/Node').addCommand('myMenuElement', 'myPythonScript.myFunction()', 'myHotkey')    # Modifiers: Shift= shift+, Alt/Option = alt+, Control/Command = ctrl+



### Create a custom menu - i.e.:
# you need a gizmo to be placed in your '.nuke' folder structure
# toolbar = nuke.menu('Nodes')
# myMenu = toolbar.addMenu('myMenuElement', icon='myMenuIcon.png')
# myMenu.addCommand('myElement', 'nuke.createNode("myGizmo")', icon='myGizmoIcon.png', index=0) #the index argument (optional) indicates the position of the item within the menu