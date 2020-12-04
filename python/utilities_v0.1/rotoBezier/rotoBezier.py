import nuke

def noBoundingBox():
    rotoList=[]
    bezierList=[]
    rotoList = nuke.selectedNodes('Roto')
    bezierList = nuke.selectedNodes('Bezier')
    if rotoList:
        for r in rotoList:
            #print r
            r.knob('cliptype').setValue('bbox')
            #nuke.selectedNodes().knob('cliptype').setValue('bbox')
    if bezierList:
        for b in bezierList:
            b.knob('cliptype').setValue('bbox')


#noBoundingBox()
