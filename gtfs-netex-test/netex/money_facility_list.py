from dataclasses import dataclass, field
from typing import List
from .money_facility_enumeration import MoneyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MoneyFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[MoneyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
