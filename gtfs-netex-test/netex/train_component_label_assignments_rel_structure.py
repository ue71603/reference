from dataclasses import dataclass, field
from typing import List, Union
from .containment_aggregation_structure import ContainmentAggregationStructure
from .train_component_label_assignment import TrainComponentLabelAssignment
from .train_component_label_assignment_ref import (
    TrainComponentLabelAssignmentRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TrainComponentLabelAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "trainComponentLabelAssignments_RelStructure"

    train_component_label_assignment_ref_or_train_component_label_assignment: List[
        Union[TrainComponentLabelAssignmentRef, TrainComponentLabelAssignment]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainComponentLabelAssignmentRef",
                    "type": TrainComponentLabelAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainComponentLabelAssignment",
                    "type": TrainComponentLabelAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
