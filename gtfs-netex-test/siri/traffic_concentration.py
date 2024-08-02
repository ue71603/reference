from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .traffic_value import TrafficValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class TrafficConcentration(TrafficValue):
    concentration: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    occupancy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    traffic_concentration_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "trafficConcentrationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
