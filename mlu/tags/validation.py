'''
mlu.tags.validation

This module contains logic responsible for the validation of a single audio file's tag values. All 
audio file tags supported by MLU are validated here.

'''

import mlu.common.time

class AudioFileTagsValidationError(Exception):
    pass

def validateAudioFileTags(audioFileTags):
    '''
    Does validation checking on an AudioFileTags object, ensuring that its current values (the tags
    currently set on the object) are valid relative to that specific tag's requirements. All tag
    validation logic is executed here.

    Throws a validation exception when a tag with an invalid value is found.

    Params:
        audioFileTags: the AudioFileTags object to validate
    '''

    _validateDateTagValue(audioFileTags.date)


def _validateDateTagValue(value):
    MIN_YEAR = 1900
    currentYear = mlu.common.time.getCurrentYear()

    if ((value < MIN_YEAR) or (value > currentYear)):
        raise AudioFileTagsValidationError("Invalid tag value: date")