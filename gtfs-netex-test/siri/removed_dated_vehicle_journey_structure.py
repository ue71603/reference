from dataclasses import dataclass, field
from typing import List, Optional

from .dated_vehicle_journey_indirect_ref_structure import DatedVehicleJourneyIndirectRefStructure
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .reason_for_removal import ReasonForRemoval
from .train_number_ref_structure import TrainNumberRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RemovedDatedVehicleJourneyStructure:
    framed_vehicle_journey_ref: FramedVehicleJourneyRefStructure = field(
        metadata={
            "name": "FramedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    dated_vehicle_journey_indirect_ref: Optional[DatedVehicleJourneyIndirectRefStructure] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyIndirectRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_numbers: Optional["RemovedDatedVehicleJourneyStructure.TrainNumbers"] = field(
        default=None,
        metadata={
            "name": "TrainNumbers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reason_for_removal: ReasonForRemoval = field(
        metadata={
            "name": "ReasonForRemoval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class TrainNumbers:
        train_number_ref: List[TrainNumberRefStructure] = field(
            default_factory=list,
            metadata={
                "name": "TrainNumberRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
