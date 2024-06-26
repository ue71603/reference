from dataclasses import dataclass, field
from typing import List

from .containment_aggregation_structure import ContainmentAggregationStructure
from .time_demand_type_assignment import TimeDemandTypeAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandTypeAssignmentsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "timeDemandTypeAssignmentsInFrame_RelStructure"

    time_demand_type_assignment: List[TimeDemandTypeAssignment] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandTypeAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
