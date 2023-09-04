'''
Disable errors v1.1, 2020-11-03

This function sets automatic disable switching for selected nodes by type.

Changelog:
- v1.2:
    - added includeList
- v1.1:
    - selects only certain kind of nodes
- v1.0:
    - selects all nodes and sets disable parameter

Written by Eugene Golubenko
eugene.golubenko@gmail.com
'''

import nuke

includeList = ['Grade', 'ColorCorrect', 'Merge2', 'HueCorrect', 'HueShift', 'Toe2', 'ColorLookup']     #add nodes here

def disableErrorsFunction():
    for node in nuke.selectedNodes():
        for i in includeList:
            if node.Class() == i:
                node['disable'].setExpression('[value error]')

