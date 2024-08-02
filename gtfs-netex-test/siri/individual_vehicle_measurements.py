from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .traffic_value import TrafficValue
from .vehicle_detection_time import VehicleDetectionTime
from .vehicle_headway import VehicleHeadway
from .vehicle_speed import VehicleSpeed

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class IndividualVehicleMeasurements(TrafficValue):
    vehicle_speed: Optional[VehicleSpeed] = field(
        default=None,
        metadata={
            "name": "vehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_detection_time: Optional[VehicleDetectionTime] = field(
        default=None,
        metadata={
            "name": "vehicleDetectionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    vehicle_headway: Optional[VehicleHeadway] = field(
        default=None,
        metadata={
            "name": "vehicleHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    individual_vehicle_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "individualVehicleMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
