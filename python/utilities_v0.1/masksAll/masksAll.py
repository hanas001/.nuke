'''
Dots all v1.0, 2020-11-09

This tool finds all dots on the snow in the shot

Changelog:
- v0.1: trying to make it work
- v0.9: organises all the channels in merge nodes, connects them to shuffle with alpha
- v1.0: added condition "if input mask is not changed - do nothing"

Written by Eugene Golubenko
eugene.golubenko@gmail.com
'''


import nuke

def collectAllMasks():
    ## taking user input for the mask to find
    pan = nuke.Panel ( 'userInput' )
    pan.addMultilineTextInput ( 'inputName' , 'type mask name to find' )
    pan.show ()
    mask = pan.value ( 'inputName' )
    # print mask

    if mask != 'type mask name to find' :   #if mask name is not changed - do nothing
        node = nuke.selectedNode ()
        channels = node.channels ()
        # print (channels)

        ## we get position of selected node
        d = nuke.createNode ( 'Dot' , inpanel=False )
        dx , dy = d.xpos () , d.ypos ()
        # nuke.delete ( d )
        offset = 140
        offset2 = 140
        # print (dx)
        # print (dy)


        shuffle = nuke.createNode ( 'Shuffle' , inpanel=False )
        shuffle.knob ( 'alpha' ).setValue ( 'black' )

        ##we create shuffle node, disconnect it and set position with offset
        shuffleNotConnected = nuke.createNode ( 'Shuffle' , inpanel=False )
        shuffleNotConnected.knob ( 'alpha' ).setValue ( 'white' )

        for i in range ( 0 , nuke.selectedNode ().maxInputs () ) :
            nuke.selectedNode ().setInput ( i , None )

        shuffleNotConnected.knob ( 'selected' ).setValue ( False )
        shuffle.knob ( 'selected' ).setValue ( True )

        for i in channels :
            channel = i.split ( '_' )
            if 'other.mask' in channel :
                if mask in channel :
                    string = '_'.join ( channel )  # string with dots
                    print ( string )
                    # node = nuke.createNode('Grade', inpanel=False)
                    merge = nuke.createNode ( 'Merge2' , inpanel=False )
                    nuke.selectedNode ().knob ( 'mask' ).setValue ( string )
                    merge.setInput ( 0 , nuke.selectedNode () )
                    merge.setInput ( 1 , shuffleNotConnected )
                    merge.setXYpos ( dx - 35 , dy + offset2 )
                    offset2 += 60

        shuffleEnd = nuke.createNode ( 'Dot' , inpanel=False )
        shuffleEnd.setXYpos ( dx , dy + offset2 )

        shuffleNotConnected.setXYpos ( dx + offset , dy + offset )