'''
mlu.tags.common

Module for functionality that is needed/shared between various other mlu.tags modules.
'''

def formatValuesListToAudioTag(valuesList):
    if (not valuesList):
        return ''
        
    listStr = ';'.join(map(str, valuesList))
    return str(listStr)

def formatAudioTagToValuesList(audioTagStr, valuesAsInt=False):
    if (not audioTagStr):
        return []
    
    valuesList = audioTagStr.split(';')

    if (valuesAsInt):
        valuesList = [int(value) for value in valuesList]
    else:
        valuesList = [str(value) for value in valuesList]

    return valuesList
