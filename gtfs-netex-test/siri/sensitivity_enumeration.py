from enum import Enum

__NAMESPACE__ = "http://www.siri.org.uk/siri"


class SensitivityEnumeration(Enum):
    VERY_HIGH = "veryHigh"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    VERY_LOW = "veryLow"
