from dataclasses import dataclass, field
from typing import List, Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .dynamic_stop_assignment import DynamicStopAssignment
from .flexible_stop_assignment import FlexibleStopAssignment
from .navigation_path_assignment import NavigationPathAssignment
from .passenger_stop_assignment import PassengerStopAssignment
from .train_stop_assignment import TrainStopAssignment
from .vehicle_journey_stop_assignment import VehicleJourneyStopAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "stopAssignmentsInFrame_RelStructure"

    stop_assignment: List[Union[VehicleJourneyStopAssignment, FlexibleStopAssignment, NavigationPathAssignment, TrainStopAssignment, DynamicStopAssignment, PassengerStopAssignment]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourneyStopAssignment",
                    "type": VehicleJourneyStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleStopAssignment",
                    "type": FlexibleStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NavigationPathAssignment",
                    "type": NavigationPathAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainStopAssignment",
                    "type": TrainStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicStopAssignment",
                    "type": DynamicStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerStopAssignment",
                    "type": PassengerStopAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
