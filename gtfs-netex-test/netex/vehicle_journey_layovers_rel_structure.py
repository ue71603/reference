from dataclasses import dataclass, field
from typing import List

from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .vehicle_journey_layover import VehicleJourneyLayover

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyLayoversRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "vehicleJourneyLayovers_RelStructure"

    vehicle_journey_layover: List[VehicleJourneyLayover] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyLayover",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
