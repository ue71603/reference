from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class EstimatedTimetableDetailEnumeration(Enum):
    MINIMUM = "minimum"
    BASIC = "basic"
    NORMAL = "normal"
    CALLS = "calls"
    FULL = "full"
