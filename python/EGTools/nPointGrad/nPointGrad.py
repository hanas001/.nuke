import nuke
import re

'''
These instructions creat and delete points
'''

def pointKnobs():
    return [p for p in nuke.thisNode().allKnobs() if re.match(r'p\d+', p.name())]

def colorKnobs():
    return [p for p in nuke.thisNode().allKnobs() if re.match(r'color\d+', p.name())]

def numberOfPointKnobs():
    return len(pointKnobs())

def addPoint():
    #print pointKnobs()
    #print numberOfPointKnobs()

    num = numberOfPointKnobs()
    node = nuke.thisNode()

    knob = nuke.Color_Knob('color{}'.format(num))
    cKnobs = colorKnobs()
    #avgColorR = sum([k.getValue(0) for k in cKnobs()]) / len(cKnobs())
    #avgColorG = sum([k.getValue(1) for k in cKnobs()]) / len(cKnobs())
    #avgColorB = sum([k.getValue(2) for k in cKnobs()]) / len(cKnobs())

    avgColor = [sum([k.getValue(i) for k in cKnobs]) / len(cKnobs) for i in range(3)] if cKnobs else [0, 0, 0]
    knob.setValue(avgColor)
    node.addKnob(knob)

    knob = nuke.XY_Knob('p{}'.format(num))
    knob.clearFlag(nuke.STARTLINE)  #creates the knob at the same line

    pKnobs = pointKnobs()
    avgPos = [sum([k.getValue(i) for k in pKnobs]) / len(pKnobs) for i in range(2)] if pKnobs else [0, 0]   #calculates average value of all colors. if knob does not exists sets 0 value
    knob.setValue(avgPos)   #sets values to the knob
    knob.clearFlag(nuke.STARTLINE)  #creates the knob at the same line
    node.addKnob(knob)  #adds the knob

    knob = nuke.PyScript_Knob('deletePoint{}'.format(num))  #creates knob 'deletePoints' with the number of the point
    knob.clearFlag(nuke.STARTLINE)  #creates the knob at the same line
    knob.setLabel('delete')
    knob.setCommand('nPointGrad.deletePoints()')
    node.addKnob(knob)  #adds the knob

    makeExpression()

def deletePoints():
    tk = nuke.thisKnob()
    tn = nuke.thisNode()
    numList = re.findall(r'deletePoint(\d+)', tk.name())
    if not numList:
        return

    num = int(numList[0])

    tn.removeKnob(tn['color{}'.format(num)])    #remeve color knob
    tn.removeKnob(tn['p{}'.format(num)])    #remove position knob
    tn.removeKnob(tk)   #remove delete knob

    while tn.knob('deletePoint{}'.format(num + 1)): #we check if there is deletePoint knob with higher value
        for k in ['color', 'p' , 'deletePoint']:    #for each value which
            knob = tn['{0}{1}'.format(k, num + 1)]  #take value of num + one
            knob.setName('{0}{1}'.format(k, num))   #rename the value to num
        num += 1    #increase step of the num

    makeExpression()

def makeExpression():   # defining function to set expression
    expressionNode = nuke.thisNode().node('Expression1')    #going to expression node inside our group

    points = pointKnobs()   #defining points from our created knobs to variable

    s = ("min({})".format(', '.join(['hypot(x - {0}.x, y - {0}.y)'.format(p.name()) for p in points])))

    expressionNode['temp_expr0'].setValue(s)

    channelDict = {'r': 'expr0', 'g': 'expr1', 'b': 'expr2'}

    for channel in channelDict.keys():

        expressionNode[channelDict[channel]].setValue(" + ".join(["(hypot(x - p{0}.x, y - p{0}.y) <= distances) * color{0}.{1}".format(re.findall(r'p(\d+)', p.name()) , channel) for p in points]))
