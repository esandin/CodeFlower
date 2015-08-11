'''
carcolours
Read a text files of fomat colour,number
and convert it to a JSON structure
where each "colour" is an indexed array with "number" children
'''

import io
import json

PARAM_TEXTFILE = 'textfile'
PARAM_JSONFILE = 'jsonfile'
CENTRE_NAME = 'Car Colours'
NAME='name'
CHILDREN='children'
SIZE='size'

def __msg__(m):
    print(str(m))
    return m


def __getparameters__():
    '''Get parameters'''
    return {PARAM_TEXTFILE:r"E:\2015\projects\CodeFlower\data\carcolours.txt"
            ,PARAM_JSONFILE:r'carcolours.json'}


def textfiletolists(path):
    '''reads a text file of format
    a,b,c 
    d,e,f 
    returns a nested list of format
    [
    [a,b,c]
    ,[d,e,f]
    ]
    '''
    lists = []
    with io.open(path,'r') as filehandle:
        for line in filehandle.readlines():
            line=line.strip('\n')
            line=line.strip('\r')
            innerlist=[]
            for item in line.split(','):
                innerlist.append(item)
            lists.append(innerlist)
    return lists

def liststodict(centrename,lists):
    '''Converts nested lists to structure
    #where each "colour" is an indexed array with "number" children'''
    jsonout = {NAME:'centrename',CHILDREN:[]}
    for innerlist in lists:
        childi={NAME:innerlist[0],CHILDREN:[]}
        for i in range(0,int(innerlist[1])):
            childi[CHILDREN].append({})
        jsonout[CHILDREN].append(childi)
    return jsonout

def liststodict2(centrename,lists):
    '''Converts nested lists to structure
    #where each "colour" is an indexed array with "number" children'''
    jsonout = {NAME:'centrename',CHILDREN:[]}
    for innerlist in lists:
        childi={NAME:innerlist[0],SIZE:int(innerlist[1])}
        jsonout[CHILDREN].append(childi)
    return jsonout


def writejsontotextfile(jsonout,outfile):
    '''Write json to text file'''
    jsonstr = json.dumps(jsonout)#,indent=2)
    with io.open(outfile,'wb') as filehandle:
        filehandle.write(jsonstr)
    return outfile


def __main__():
    #Get parameters
    paramdict=__getparameters__()
    #reads a text file ... returns a nested list of format
    lists = textfiletolists(paramdict[PARAM_TEXTFILE])
    #Convert it to a JSON structure
    #where each "colour" is an indexed array with "number" children
    jsonout = liststodict(CENTRE_NAME,lists)
    #write json to text file
    writejsontotextfile(jsonout,paramdict[PARAM_JSONFILE])
    return None

if __name__ == '__main__':
    __main__()