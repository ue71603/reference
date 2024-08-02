from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .maintenance_vehicles import MaintenanceVehicles
from .mobility import Mobility
from .operator_action import OperatorAction
from .roadworks_duration_enum import RoadworksDurationEnum
from .roadworks_scale_enum import RoadworksScaleEnum
from .subjects import Subjects

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Roadworks(OperatorAction):
    roadworks_duration: Optional[RoadworksDurationEnum] = field(
        default=None,
        metadata={
            "name": "roadworksDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadworks_scale: Optional[RoadworksScaleEnum] = field(
        default=None,
        metadata={
            "name": "roadworksScale",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    under_traffic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "underTraffic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    urgent_roadworks: Optional[bool] = field(
        default=None,
        metadata={
            "name": "urgentRoadworks",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    mobility: Optional[Mobility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    subjects: Optional[Subjects] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    maintenance_vehicles: Optional[MaintenanceVehicles] = field(
        default=None,
        metadata={
            "name": "maintenanceVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    roadworks_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "roadworksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
