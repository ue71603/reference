from dataclasses import dataclass, field
from typing import List

from .ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingServiceFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
