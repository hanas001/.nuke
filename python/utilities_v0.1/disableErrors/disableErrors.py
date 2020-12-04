'''
Disable errors v1.1, 2020-11-03

This function sets automatic disable switching for selected nodes by type.

Changelog:
- v1.1:
    - selects only certain kind of nodes
- v1.0:
    - selects all nodes and sets disable parameter

Written by Eugene Golubenko
eugene.golubenko@gmail.com
'''

import nuke

def disableErrorsFunction():
    for node in nuke.selectedNodes():
        if node.Class() == 'Grade' or node.Class() == 'ColorCorrect' or node.Class() =='Merge2':
            node['disable'].setExpression('[value error]')