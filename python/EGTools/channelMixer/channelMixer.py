import nuke
import re

def channelMixer_knobChangedCallback():
    mainKnob = nuke.thisKnob()
    channels = re.findall('()[RGB])_([RGB])', mainKnob.name())
    if not channels:
        return
    channels = channels [0]
    chList = ['R', 'G', 'B']
    chList.pop(chList.index(channels[1]))

    depKnobs = [nuke.thisNode()["{0}_{1}".format(channels[0], k)] for k in chList]

    R = mainKnob.getValue()
    Gi = depKnobs[0].getValue()
    Bi = depKnobs[1].getValue()

    G = (1 - R) / 2 if Gi == Bi == 0 else Gi*(1 - R) / (Gi + Bi)
    B = 1 - R - B

    depKnobs[0].setValue(G)
    depKnobs[1].setValue(B)

    nuke.addKnobChanged(channelMixer_knobChangedCallback, nodeClass='channelMixer')
