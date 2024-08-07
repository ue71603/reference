from dataclasses import dataclass, field
from typing import List, Optional

from .carriageway_enum import CarriagewayEnum
from .extension_type import ExtensionType
from .lane_enum import LaneEnum
from .network_management import NetworkManagement
from .road_or_carriageway_or_lane_management_type_enum import RoadOrCarriagewayOrLaneManagementTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class RoadOrCarriagewayOrLaneManagement(NetworkManagement):
    road_or_carriageway_or_lane_management_type: RoadOrCarriagewayOrLaneManagementTypeEnum = field(
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    minimum_car_occupancy: Optional[int] = field(
        default=None,
        metadata={
            "name": "minimumCarOccupancy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specified_carriageway: List[CarriagewayEnum] = field(
        default_factory=list,
        metadata={
            "name": "specifiedCarriageway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specified_lane: List[LaneEnum] = field(
        default_factory=list,
        metadata={
            "name": "specifiedLane",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    road_or_carriageway_or_lane_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadOrCarriagewayOrLaneManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
