'''
Highest version v0.1, 2020-12-03

This tool makes the version of selected node the newest

Changelog:
- v0.1: trying to make it work
-
-

Written by Eugene Golubenko
eugene.golubenko@gmail.com
'''

import nuke
import os
import sys

nodeSelected = nuke.selectedNode ()
fileName = nodeSelected.knob ( 'file' ).value ()
print ( fileName )

# print (nodeSelected)
layer = fileName.split ( '/' ) [ -2 ]
# print (layer)

version = fileName.split ( '/' ) [ -3 ]
# print (version)

osPath = [ ]
inPath = fileName.split ( '/' ) [ :-3 ]

print ( inPath )
for i in inPath :
    print ( i )
    osPath += os.sep + i

# print (type(inPath))


# if sys.platform == "win32":
#    osPath = inPath.replace('/', os.sep)    #chenges slash to back slash in windows OS

print ( str ( osPath ) )