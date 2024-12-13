from enum import StrEnum


class ReferenceFrameType(StrEnum):

    GCRS = "GCRS"
    ITRS = "ITRS"


class ReferenceFrame(object):

    def __init__(self, type: ReferenceFrameType):
        pass
