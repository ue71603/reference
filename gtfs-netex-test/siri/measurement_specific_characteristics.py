from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .lane_enum import LaneEnum
from .measured_or_derived_data_type_enum import MeasuredOrDerivedDataTypeEnum
from .vehicle_characteristics import VehicleCharacteristics

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class MeasurementSpecificCharacteristics:
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specific_lane: Optional[LaneEnum] = field(
        default=None,
        metadata={
            "name": "specificLane",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    specific_measurement_value_type: MeasuredOrDerivedDataTypeEnum = field(
        metadata={
            "name": "specificMeasurementValueType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    specific_vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "specificVehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_specific_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSpecificCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
