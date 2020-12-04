import os
import re
import nuke

# name = '\\omega\leo\3_post\me011\sh0249\comp\me011_sh0249_comp_v001.nk'

node_read = [ ]
node_text = [ ]


def contactSheetFunction() :
    name = nuke.root ().name ()  # root name

    ## we create dot, take its positipon for further use
    d = nuke.createNode ( 'Dot' )
    dx , dy = d.xpos () , d.ypos ()
    nuke.delete ( d )

    ##we split the name and do the magic
    sq = name.split ( '/' ) [ 5 ]
    sq_file = name.split ( sq ) [ 0 ] + sq
    # print (sq_file)
    sq_list = [ i for i in os.listdir ( sq_file ) if os.path.isdir ( sq_file + '/' + i ) if 'sh' in i ]
    sq_list.sort ()
    print ( sq_list )

    # node_read = [ ]
    # node_text = [ ]

    x , y = 0 , 0
    for k in sq_list :
        out = sq_file + '/' + k + '/out'
        if os.path.exists ( out ) :
            maksV = out + '/' + max ( [ i for i in os.listdir ( out ) if os.path.isdir ( out + '/' + i ) ] )

            r_file = ''
            fr_first = 1
            fr_last = 1

            img_list = os.listdir ( maksV )
            img_files = [ i for i in img_list if re.match ( '.*[0-9][0-9][0-9][0-9][0-9]*' , i ) ]
            img_files.sort ()

            if len ( img_files ) > 1 :
                XXXX = img_files [ 0 ]
                r_file = maksV + '/' + XXXX.split ( '.' ) [ 0 ] + '.%05d.' + XXXX.split ( '.' ) [ -1 ]
                fr_first = int ( img_files [ 0 ].split ( '.' ) [ 1 ] )
                fr_last = int ( img_files [ -1 ].split ( '.' ) [ 1 ] )
            else :
                if len ( img_files ) :
                    XXXX = img_files [ 0 ]
                    r_file = maksV + '/' + XXXX

            if fr_first != fr_last :  # removes empty folders
                node = nuke.nodes.Read ()
                node [ 'file' ].setValue ( r_file )
                # print (r_file)
                node [ 'first' ].setValue ( fr_first )
                node [ 'last' ].setValue ( fr_last )
                node [ 'origfirst' ].setValue ( fr_first )
                node [ 'origlast' ].setValue ( fr_last )

                text = nuke.nodes.Text2 ()
                text [ 'message' ].setValue ( out.split ( '/' ) [ -2 ] )  # insert name of the shot to Text node
                text [ 'yjustify' ].setValue ( 'bottom' )
                text.setInput ( 0 , node )  # connects Text node to Read
                node_text.append ( text )  # amount of text nodes

                node.setXYpos ( x , y )

                x = x + 100
                node_read.append ( node )

                # print (node_read)

    lines = 5  # number of tiles in a line
    x , y = dx , dy
    xx , yy = 110 , 140
    c , d = 0 , 1
    for n in node_read :
        n.setXYpos ( x + xx * c , y + yy * d )
        if c < lines - 1 :
            c = c + 1
        else :
            c = 0
            d = d + 1

    ##width and height of the tiles
    current_width = nuke.root () [ "format" ].value ().width ()
    current_height = nuke.root () [ "format" ].value ().height ()
    X = current_width
    Y = current_height / lines * d

    ##we create contact sheet node and connect read nodes to it
    c_sh = nuke.nodes.ContactSheet ()
    c_sh [ 'width' ].setValue ( X )
    c_sh [ 'height' ].setValue ( Y )
    c_sh [ 'rows' ].setValue ( d )
    c_sh [ 'columns' ].setValue ( lines )
    c_sh [ 'roworder' ].setValue ( 'TopBottom' )
    c_sh.setXYpos ( dx + xx * 6 , dy + yy )
    for i in range ( len ( node_text ) ) :  # connect Text nodes to ContactSheet
        c_sh.setInput ( i , node_text [ i ] )
    # print (node_text)
    # print (len (node_text))


#contactSheetFunction ()