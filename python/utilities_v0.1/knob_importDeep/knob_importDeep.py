import nuke, nukescripts
import os, re, string
import _metaProject

reload(_metaProject)


def start_importDeep():
    print('knob_importDeep')
    # sources ################
    p_Index = _metaProject.p_Index()
    # mt_fold     = 'C:/Parovoz/tools30/nuke/plugins/prvz/metaProject'   #os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    mt_fold = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')

    pkey = p_Index[1].keys();
    pkey.sort()
    info_file = mt_fold + '/' + '_info' + '/' + p_Index[0] + '_root.txt'

    Server_file = os.getenv('PRVZ_PROJECT_PATH') + '/3_post'

    RT = _metaProject.N_root_proj(Server_file, info_file, pkey)
    pNp = {p: p_Index[2][p] for p in pkey}
    # print(RT, 'rt')
    # print(pNp, 'pNp')

    p_sire = pNp[RT['_sire_']]  # 'me030'
    p_low = pNp[RT['_low_']]  # 'sh0230'
    ################
    ImpDeep_(p_sire, p_low)

def ImpDeep_(p_sire, p_low):
    # p_sire , p_low  = nuke.root().name().split('/')[-1].split('_')[0:2]
    # p_sire='ep035' , p_low='sh0106'

    #print(p_sire, p_low)

    f = os.getenv('PRVZ_PROJECT_PATH') + '/3_post/' + p_sire + '/' + p_low + '/in/'
    # print(f, 'this is path F')
    #//omega/catsdogs/3_post/ep141/sh0120/in/

    contents = os.listdir(f)
    folders = [item for item in contents if os.path.isdir(os.path.join(f))]
    # file_in = P_01_file + '/' + P_02 + '/in'
    # print(folders, 'folders')
    # folderList = {}
    fversion = str
    for versionFolder in folders:
        if re.match(r'^v\d{3}$', versionFolder):
            fversion = f + versionFolder
            # print(fversion, 'path ending with v000')
            # print(f, 'this is path to file ending in  "IN"')
            # print(versionFolder, 'this is version folder')


            contentsLayers = os.listdir(fversion)
            layers = [item for item in contentsLayers if os.path.isdir(os.path.join(fversion))]

            for layer in layers:
                fLayerVersion = fversion + "/" + layer + "/"
                # print(fLayerVersion, '>>>>>>>>>>>>>>this is file Layer')


                deepFolders = os.listdir(fLayerVersion)
                deepFolder = [item for item in deepFolders if os.path.isdir(os.path.join(fLayerVersion))]

                for folder in deepFolder:
                    if re.match(r'^.*deep.*$', folder):
                        # print(folder, 'i am folder')
                        fDeepVersion = fLayerVersion + folder + "/"


                        #deep_ep141_sh0503_render_v001.####.exr path example
                        #block of code to set out the name of deep files
                        # fileName = str
                        fileName = 'deep_' + p_sire  +'_'+ p_low +'_' + 'render' + "_" + versionFolder + '.####.exr'
                        # print(fileName, '>>>>>file name<<<<<<<')

                        #range of the sequence
                        exr = os.listdir(fDeepVersion)
                        exr.sort()
                        exr = [i for i in exr if 'exr' in i]
                        fr_first = int(exr[0].split('.')[1])
                        fr_last = int(exr[-1].split('.')[1])


                        deepFiles = fDeepVersion + fileName

                        deepNode = nuke.createNode('DeepRead')
                        # deepNode['read_from_file'].setValue(True)
                        # deepNode['frame_rate'].setValue(25)
                        deepNode['file'].setValue(deepFiles)
                        deepNode['label'].setValue(layer)
                        deepNode['first'].setValue(fr_first)
                        deepNode['last'].setValue(fr_last)