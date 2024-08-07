from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class RemedyTypeEnumeration(Enum):
    UNKNOWN = "unknown"
    REPLACE = "replace"
    REPAIR = "repair"
    REMOVE = "remove"
    OTHER_ROUTE = "otherRoute"
    OTHER_LOCATION = "otherLocation"
